from flask import Flask, request, jsonify

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

if __name__ == '__main__':
    app.run()
