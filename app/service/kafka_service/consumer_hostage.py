import os
from dotenv import load_dotenv
from kafka import KafkaConsumer
import json

load_dotenv(verbose=True)
def process_hostage_messages():
    consumer = KafkaConsumer(
        os.getenv('TOPIC_MESSAGES_HOSTAGE_NAME'),
        bootstrap_servers=os.getenv('BOOTSTRAP_SERVERS'),
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='email-processor',
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )

    print("Starting hostage consumer...")
    try:
        for message in consumer:
            email_data = message.value
            print(f"Hostage saved to database: {email_data}")
    except Exception as e:
        print(f"Consumer error: {e}")
    finally:
        consumer.close()

if __name__ == '__main__':
    try:
        process_hostage_messages()
    except KeyboardInterrupt:
        print("\nShutting down consumer...")
