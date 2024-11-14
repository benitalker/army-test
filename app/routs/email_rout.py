from flask import Flask, request, jsonify
from app.database.connect import emails

app = Flask(__name__)

@app.route('/api/email', methods=['POST'])
def receive_email():
    data = request.get_json()

    if data is None:
        return jsonify({"error": "Invalid JSON data"}), 400

    result = emails.insert_one(data)

    data["_id"] = str(result.inserted_id)

    return jsonify({
        data
    }), 200

if __name__ == '__main__':
    app.run(debug=True)
