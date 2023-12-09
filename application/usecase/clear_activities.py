from infra.repository.activities_repository_database import ActivitiesRepositoryDatabase
from infra.database.concrete_mongo_adapter import ConcreteMongoAdapter


class ClearActivities:

    def __init__(self, repository: ActivitiesRepositoryDatabase(ConcreteMongoAdapter())):
        self.repository = repository

    def execute(self):
        self.repository.delete_many()
