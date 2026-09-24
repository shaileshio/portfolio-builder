from fastapi import APIRouter, HTTPException
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from app.db.session import AsyncSessionDep

from .schemas import HealthReadyErrorResponse, HealthReadyResponse, HealthResponse

router = APIRouter(prefix="/health", tags=["Health"])


@router.get("/")
async def health() -> HealthResponse:
    return HealthResponse(status="ok")


@router.get(
    "/ready",
    responses={503: {"model": HealthReadyErrorResponse}},
)
async def ready(session: AsyncSessionDep) -> HealthReadyResponse:
    try:
        await session.execute(text("SELECT 1"))

        return HealthReadyResponse(status="ok", database="connected")
    except SQLAlchemyError:
        raise HTTPException(
            status_code=503,
            detail={
                "status": "error",
                "database": "disconnected",
            },
        )
