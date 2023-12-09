from infra.database.concrete_mongo_adapter import ConcreteMongoAdapter
from infra.repository.activities_repository_database import ActivitiesRepositoryDatabase


class GetActivities:

    def __init__(self):
        self.activities = []

    def execute(self):
        repository = ActivitiesRepositoryDatabase(ConcreteMongoAdapter())
        self.activities = repository.connection.find('')
        return self.activities

