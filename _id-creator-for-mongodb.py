from pymongo import MongoClient
from pymongo.server_api import ServerApi


def database_connection():
    myclient = MongoClient('mongodb://localhost:27017', server_api=ServerApi('1'))
    mydb = myclient['test']
    return mydb

db = database_connection()
collection = db.test_collection


def insert_to_mongodb():
    data_list = [{'model': 'BMW 230', 'mpg': '27.5'}, {'model': 'Ford Edge', 'mpg': '24.1'}]
    id_creator(data_list)
    collection.insert_many(data_list)

def id_creator(data_list):
    if collection.count_documents({})>0: #if collection exists, _id starts with last _id of connection + 1
        start_id = collection.find().sort('_id' , 1)[0]['_id'] + 1
        for new_id, d in enumerate(data_list, start=start_id):
            d['_id'] = new_id
    else:
        for new_id, d in enumerate(data_list, start=1): #if collection doesn't exist, _id starts withs 1
            d['_id'] = new_id
