import os
from dotenv import load_dotenv
from kafka import KafkaConsumer
import json
from app.database.mongo_connect import emails

load_dotenv(verbose=True)
def process_emails():
    consumer = KafkaConsumer(
        os.getenv('TOPIC_MESSAGES_ALL_NAME'),
        bootstrap_servers=os.getenv('BOOTSTRAP_SERVERS'),
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='email-processor',
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )

    print("Starting email consumer...")
    try:
        for message in consumer:
            email_data = message.value
            emails.insert_one(email_data)
            print(f"Email saved to database: {email_data}")
    except Exception as e:
        print(f"Consumer error: {e}")
    finally:
        consumer.close()

if __name__ == '__main__':
    try:
        process_emails()
    except KeyboardInterrupt:
        print("\nShutting down consumer...")
