import pymongo
from interfaces.repository_interface import RepositoryInterface


class ConcreteMongoAdapter(RepositoryInterface):
    def __init__(self, db_name='db_strava', collection_name='activities'):
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def insert_one(self, document):
        return self.collection.insert_one(document)

    def insert_many(self, documents):
        return self.collection.insert_many(documents)

    def find(self, query=''):
        return self.collection.find(query)

    def update_one(self, query, update):
        return self.collection.update_one(query, update)

    def delete_one(self, query):
        return self.collection.delete_one(query)

    def delete_many(self):
        return self.collection.delete_many({})

    def close_connection(self):
        self.client.close()
