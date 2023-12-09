from abc import ABC, abstractmethod
from typing import List
from domain.activity import Activity


class StravaGatewayInterface(ABC):
    @abstractmethod
    def get_activities_batch(self, page: int, per_page: int) -> List[Activity]:
        pass
