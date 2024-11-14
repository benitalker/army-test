import json
import os
from dotenv import load_dotenv
from kafka import KafkaProducer

load_dotenv(verbose=True)

def publish_email(email_data):
    producer = KafkaProducer(
        bootstrap_servers=os.environ['BOOTSTRAP_SERVERS'],
        value_serializer=lambda v: json.dumps(v).encode('utf-8'),
    )
    producer.send(
        os.environ['TOPIC_MESSAGES_ALL_NAME'],
        value=email_data
    )
    producer.flush()

def publish_explosive(email_data):
    producer = KafkaProducer(
        bootstrap_servers=os.environ['BOOTSTRAP_SERVERS'],
        value_serializer=lambda v: json.dumps(v).encode('utf-8'),
    )
    producer.send(
        os.environ['TOPIC_MESSAGES_EXPLOSIVE_NAME'],
        value=email_data
    )
    producer.flush()

def publish_hostage(email_data):
    producer = KafkaProducer(
        bootstrap_servers=os.environ['BOOTSTRAP_SERVERS'],
        value_serializer=lambda v: json.dumps(v).encode('utf-8'),
    )
    producer.send(
        os.environ['TOPIC_MESSAGES_HOSTAGE_NAME'],
        value=email_data
    )
    producer.flush()
