from fastapi import FastAPI, APIRouter, HTTPException
from infra.middleware.exception_handlers import setup_exception_handlers
from application.usecase.calculate_metrics_per_year import CalculateMetricsPerYear
from application.usecase.calculate_evolution_of_year import CalculateEvolutionOfYear
from infra.gateway.strava_gateway_http import StravaGatewayHttp
from application.usecase.get_activities import GetActivities

app = FastAPI()

setup_exception_handlers(app)

router = APIRouter()


@router.get("/per_year")
def metrics_per_year():
    try:
        get_activity = GetActivities()
        activities = get_activity.execute()
        use_case = CalculateMetricsPerYear(activities)
        return use_case.execute()
    except HTTPException as e:
        return {"error_message": str(e), "status_code": e.status_code}


@router.get("/evolution_of_year/{year}/{year_comparation}")
def evolution_of_year(year: int, year_comparation: int):
    try:
        get_activity = GetActivities()
        activities = get_activity.execute()
        use_case = CalculateEvolutionOfYear(activities, year, year_comparation)
        return use_case.execute()
    except HTTPException as e:
        return {"error_message": str(e), "status_code": e.status_code}


@router.get("/token")
def token():
    return StravaGatewayHttp().get_token()


app.include_router(router)
