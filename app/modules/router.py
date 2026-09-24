from fastapi import APIRouter

from .auth.router import router as auth_router
from .health.router import router as health_router

router = APIRouter()

router.include_router(health_router)
router.include_router(auth_router)
