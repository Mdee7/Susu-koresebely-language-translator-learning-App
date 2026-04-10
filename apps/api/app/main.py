from fastapi import FastAPI

from app.routes.health import router as health_router
from app.routes.translate import router as translate_router

app = FastAPI(title="Susu Language Platform API", version="0.1.0")

app.include_router(health_router, tags=["system"])
app.include_router(translate_router, prefix="/v1", tags=["translation"])
