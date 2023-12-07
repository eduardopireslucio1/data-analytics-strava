from infra.gateway.strava_gateway_http import StravaGatewayHttp
from fastapi import APIRouter, HTTPException
from application.usecase.persist_activities import PersistActivities
from fastapi.responses import JSONResponse
router = APIRouter()


@router.post("/activities")
def persist_activities():
    try:
        gateway = StravaGatewayHttp()
        activities = gateway.get_activities()
        if any('message' in activity for activity in activities):
            error = {
                "message": activities.get('message')
            }
            raise HTTPException(status_code=400, detail=error)
        use_case = PersistActivities(activities)
        return use_case.execute()
    except HTTPException as e:
        return JSONResponse(content=e.detail, status_code=e.status_code)
