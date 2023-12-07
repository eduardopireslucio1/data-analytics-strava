from application.repository.mongo_adapter import MongoAdapter


class ActivitiesRepositoryDatabase:
    def __init__(self, connection: MongoAdapter):
        self.connection = connection

    def insert_many(self, activities):
        result = self.connection.insert_many(activities)
