from collections.abc import AsyncGenerator
from typing import Annotated

from fastapi import Depends

from .session import AsyncSession, AsyncSessionLocal


async def get_async_session() -> AsyncGenerator[AsyncSession]:
    async with AsyncSessionLocal() as session:
        yield session


type AsyncSessionDep = Annotated[AsyncSession, Depends(get_async_session)]
