from pymongo import MongoClient

client = MongoClient('mongodb://172.20.179.219:27017')
all_messages = client['all_messages']
emails = all_messages['emails']
