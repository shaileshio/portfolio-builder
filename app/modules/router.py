from fastapi import APIRouter

from .health.router import router as health_router

router = APIRouter()

router.include_router(health_router, prefix="/health", tags=["Health"])
