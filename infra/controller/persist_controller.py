from fastapi import APIRouter, HTTPException, Depends
from application.usecase.persist_activities import PersistActivities
from fastapi.responses import JSONResponse
from infra.repository.activities_repository_database import ActivitiesRepositoryDatabase
from infra.database.concrete_mongo_adapter import ConcreteMongoAdapter
from infra.gateway.strava_gateway_http import StravaGatewayHttp
from interfaces.strava_gateway_interface import StravaGatewayInterface
from interfaces.repository_interface import RepositoryInterface

router = APIRouter()


def get_gateway():
    return StravaGatewayHttp()


def get_repository():
    return ActivitiesRepositoryDatabase(ConcreteMongoAdapter())


@router.post("/activities")
def persist_activities(gateway: StravaGatewayInterface = Depends(get_gateway),
                       repository: RepositoryInterface = Depends(get_repository)):
    try:
        use_case = PersistActivities(gateway, repository)
        return use_case.execute()
    except HTTPException as e:
        return JSONResponse(content=e.detail, status_code=e.status_code)
