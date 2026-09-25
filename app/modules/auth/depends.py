from typing import Annotated

from fastapi import Depends

from app.db.depends import AsyncSessionDep
from app.db.repositories.user import UserRepository

from .service import UserService


def get_user_service(session: AsyncSessionDep) -> UserService:
    return UserService(UserRepository(session))


type UserServiceDep = Annotated[UserService, Depends(get_user_service)]
