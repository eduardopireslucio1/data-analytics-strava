from abc import ABC, abstractmethod


class RepositoryInterface(ABC):
    @abstractmethod
    def insert_one(self, document):
        pass

    @abstractmethod
    def insert_many(self, documents):
        pass

    @abstractmethod
    def find(self, query):
        pass

    @abstractmethod
    def update_one(self, query, update):
        pass

    @abstractmethod
    def delete_one(self, query):
        pass

    @abstractmethod
    def delete_many(self):
        pass

    @abstractmethod
    def close_connection(self):
        pass
