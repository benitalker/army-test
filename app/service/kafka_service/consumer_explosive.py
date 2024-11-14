import os
from dotenv import load_dotenv
from kafka import KafkaConsumer
import json

from app.repository.User_repository import insert_user

load_dotenv(verbose=True)
def process_explosive_messages():
    consumer = KafkaConsumer(
        os.getenv('TOPIC_MESSAGES_EXPLOSIVE_NAME'),
        bootstrap_servers=os.getenv('BOOTSTRAP_SERVERS'),
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='email-processor',
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )

    print("Starting explosive consumer...")
    try:
        for message in consumer:
            email_data = message.value
            insert_user(email_data)
            print(f"Explosive saved to database: {email_data}")
    except Exception as e:
        print(f"Consumer error: {e}")
    finally:
        consumer.close()

if __name__ == '__main__':
    try:
        process_explosive_messages()
    except KeyboardInterrupt:
        print("\nShutting down consumer...")
