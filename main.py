from fastapi import FastAPI
from infra.controller import metrics_controller
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

app.include_router(metrics_controller.router, prefix="/metrics")
