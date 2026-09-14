from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from app.core.config import Settings, get_settings

settings: Settings = get_settings()


DATABASE_URL: str | None = settings.database.url

if DATABASE_URL is None:
    raise OSError("Database url not found.")


engine: AsyncEngine = create_async_engine(
    url=DATABASE_URL,
    pool_pre_ping=True,
)


AsyncSessionLocal: async_sessionmaker[AsyncSession] = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    autoflush=False,
    expire_on_commit=False,
)


async def get_db() -> AsyncGenerator[AsyncSession]:
    async with AsyncSessionLocal() as session:
        yield session
