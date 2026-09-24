from fastapi import APIRouter

from app.db.models.user import User
from app.db.session import AsyncSessionDep

from .dependencies import UserServiceDep
from .schemas import LoginRequest, LogoutRequest, RegisterRequest, RegisterResponse

router = APIRouter(prefix="/auth", tags=["Authencation"])


@router.post("/register", response_model=RegisterResponse)
async def register(data: RegisterRequest, service: UserServiceDep) -> User:
    return await service.create_active_user(data)


@router.post("/login")
async def login(data: LoginRequest, session: AsyncSessionDep): ...


@router.post("/logout")
async def logout(data: LogoutRequest, session: AsyncSessionDep): ...
