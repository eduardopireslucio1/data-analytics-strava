from interfaces.repository_interface import RepositoryInterface


class ActivitiesRepositoryDatabase:
    def __init__(self, connection: RepositoryInterface):
        self.connection = connection

    def insert_many(self, activities):
        try:
            self.connection.insert_many(activities)
        except Exception as e:
            raise 'fails to insert activities'

    def delete_many(self):
        self.connection.delete_many()
