from interfaces.strava_gateway_interface import StravaGatewayInterface
from application.usecase.clear_activities import ClearActivities
from interfaces.repository_interface import RepositoryInterface
from fastapi.responses import JSONResponse


class PersistActivities:
    MESSAGE_SUCCESS = 'Data persisted successfully'

    def __init__(self, gateway: StravaGatewayInterface, repository: RepositoryInterface):
        self.gateway = gateway
        self.repository = repository

    def execute(self, page: int = 1, per_page: int = 100):
        ClearActivities(self.repository).execute()
        while True:
            activities = self.gateway.get_activities_batch(page, per_page)
            if not activities:
                break
            self.repository.insert_many(activities)
            page += 1
        return JSONResponse({"message": self.MESSAGE_SUCCESS})
