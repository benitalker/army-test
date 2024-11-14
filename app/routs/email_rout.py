from collections import Counter
from flask import request, jsonify, Blueprint
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import joinedload
from app.database.psql_connect import session_maker
from app.models import User, HostageSentence, ExplosiveSentence
from app.service.email_service import check_if_contains_suspicious_content, get_suspicious_content, get_most_common_word
from app.service.kafka_service.producer import publish_email

email_blueprint = Blueprint("email", __name__)

@email_blueprint.route('/email', methods=['POST'])
def receive_email():
    email_data= request.get_json()
    if email_data is None:
        return jsonify({"error": "Invalid JSON data"}), 400
    publish_email(email_data)
    check_if_contains_suspicious_content(email_data)
    return jsonify(email_data), 200

@email_blueprint.route('/suspicious_content/<string:email>', methods=['GET'])
def get_suspicious_emails_content(email):
    try:
        response_data, error = get_suspicious_content(email)
        if error:
            return jsonify({"message": error}), 404
        return jsonify(response_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@email_blueprint.route('/most_common_word', methods=['GET'])
def get_most_common_word_route():
    try:
        most_common_word, frequency = get_most_common_word()
        return jsonify({"most_common_word": most_common_word, "frequency": frequency})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
