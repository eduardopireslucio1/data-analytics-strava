from fastapi import APIRouter, HTTPException
from application.usecase.calculate_metrics_per_year import CalculateMetricsPerYear
from infra.gateway.strava_gateway_http import StravaGatewayHttp
from fastapi.responses import JSONResponse
import os

router = APIRouter()


@router.get("/per_year")
def metrics_per_year():
    try:
        gateway = StravaGatewayHttp()
        activities = gateway.get_activities()
        if any('message' in activity for activity in activities):
            error = {
                "message": activities.get('message')
            }
            raise HTTPException(status_code=400, detail=error)
        use_case = CalculateMetricsPerYear(activities)
        return use_case.execute()
    except HTTPException as e:
        return JSONResponse(content=e.detail, status_code=e.status_code)
