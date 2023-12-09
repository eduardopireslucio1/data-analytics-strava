from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse


def setup_exception_handlers(app: FastAPI):
    @app.exception_handler(HTTPException)
    async def http_exception_handler(request, exc):
        return JSONResponse(content=exc.detail, status_code=exc.status_code)
