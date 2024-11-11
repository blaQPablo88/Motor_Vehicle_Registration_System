from pymongo import MongoClient

uri = 'mongodb://localhost:27017/'
client = MongoClient(uri)
database = client.get_database('dltc_db')
collection = database.get_collection('vehicles')

