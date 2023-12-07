from fastapi import FastAPI
from infra.controller import metrics_controller
from infra.controller import persist_controller
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

app.include_router(metrics_controller.router, prefix="/metrics")
app.include_router(metrics_controller.router, prefix="/token")

app.include_router(persist_controller.router, prefix="/persist")


