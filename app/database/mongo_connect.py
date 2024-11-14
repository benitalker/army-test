import os
from pymongo import MongoClient

client = MongoClient(os.getenv('MONGO_CONNECT'))
all_messages = client['all_messages']
emails = all_messages['emails']
