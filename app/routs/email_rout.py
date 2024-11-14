from collections import Counter

from flask import Flask, request, jsonify
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import joinedload

from app.database.psql_connect import session_maker
from app.models import User, HostageSentence, ExplosiveSentence
from app.service.email_service import check_if_contains_suspicious_content
from app.service.kafka_service.producer import publish_email

app = Flask(__name__)

@app.route('/api/email', methods=['POST'])
def receive_email():
    email_data= request.get_json()
    if email_data is None:
        return jsonify({"error": "Invalid JSON data"}), 400
    publish_email(email_data)
    check_if_contains_suspicious_content(email_data)
    return jsonify(email_data), 200

@app.route('/api/suspicious_content/<string:email>', methods=['GET'])
def get_suspicious_content(email):
    try:
        with session_maker() as session:
            user = (
                session.query(User)
                .options(joinedload(User.hostage_sentences), joinedload(User.explosive_sentences))
                .filter_by(email=email)
                .first()
            )
            if not user:
                return jsonify({"message": "User not found"}), 404
            hostage_sentences = [sentence.sentence for sentence in user.hostage_sentences]
            explosive_sentences = [sentence.sentence for sentence in user.explosive_sentences]

            return jsonify({
                "email": email,
                "hostage_sentences": hostage_sentences,
                "explosive_sentences": explosive_sentences
            })
    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500

# @app.route('/api/most_common_word', methods=['GET'])
# def get_most_common_word():
#     try:
#         with session_maker() as session:
#             all_sentences = (
#                 session.query(HostageSentence.sentence)
#                 .union(session.query(ExplosiveSentence.sentence))
#                 .all()
#             )
#             words = [word.lower() for sentence in all_sentences for word in sentence[0].split()]
#             word_counts = Counter(words).most_common(1)
#
#             if word_counts:
#                 most_common_word, frequency = word_counts[0]
#                 return jsonify({"most_common_word": most_common_word, "frequency": frequency})
#             else:
#                 return jsonify({"message": "No words found"}), 404
#     except SQLAlchemyError as e:
#         return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run()
