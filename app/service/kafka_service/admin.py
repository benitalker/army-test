import os
from dotenv import load_dotenv
from kafka import KafkaAdminClient
from kafka.admin import NewTopic
from kafka.errors import TopicAlreadyExistsError

load_dotenv(verbose=True)

def init_topics():
    client = KafkaAdminClient(bootstrap_servers=os.environ['BOOTSTRAP_SERVERS'])
    topic_names = [
        os.environ['TOPIC_GYM_MEMBERSHIP_NAME'],
        os.environ['TOPIC_GYM_CLASSES_NAME'],
        os.environ['TOPIC_GYM_EQUIPMENT_NAME'],
    ]
    topics = [
        NewTopic(
            t,
            num_partitions=int(os.environ['NUMBER_OF_PARTITION']),
            replication_factor=int(os.environ['NUMBER_OF_REPLICATION']),
        )
        for t in topic_names
    ]

    try:
        client.create_topics(topics)
    except TopicAlreadyExistsError as e:
        print(str(e))
    finally:
        client.close()

if __name__ == '__main__':
    init_topics()
