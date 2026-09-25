from collections.abc import AsyncGenerator

import pytest_asyncio
from httpx import ASGITransport, AsyncClient
from sqlalchemy.ext.asyncio import (
    AsyncConnection,
    AsyncEngine,
    AsyncSession,
    create_async_engine,
)

from app.core.config import get_settings
from app.db.depends import get_async_session
from app.main import app

settings = get_settings()

TEST_DATABASE_URL = settings.database.test_url

if TEST_DATABASE_URL is None:
    raise OSError("Test database URL not found.")


@pytest_asyncio.fixture
async def async_engine() -> AsyncGenerator[AsyncEngine]:
    engine = create_async_engine(
        TEST_DATABASE_URL,  # type: ignore
        echo=False,
        pool_pre_ping=True,
    )

    try:
        yield engine
    finally:
        await engine.dispose()


@pytest_asyncio.fixture
async def async_connection(
    async_engine: AsyncEngine,
) -> AsyncGenerator[AsyncConnection]:
    async with async_engine.connect() as connection:
        transaction = await connection.begin()

        try:
            yield connection
        finally:
            if transaction.is_active:
                await transaction.rollback()


@pytest_asyncio.fixture
async def async_session(
    async_connection: AsyncConnection,
) -> AsyncGenerator[AsyncSession]:
    session = AsyncSession(
        bind=async_connection,
        expire_on_commit=False,
        join_transaction_mode="create_savepoint",
    )

    try:
        yield session
    finally:
        await session.close()


@pytest_asyncio.fixture
async def async_client(async_session: AsyncSession) -> AsyncGenerator[AsyncClient]:

    async def get_async_test_session() -> AsyncGenerator[AsyncSession]:
        yield async_session

    app.dependency_overrides[get_async_session] = get_async_test_session

    try:
        transport = ASGITransport(app=app)

        async with AsyncClient(
            transport=transport,
            base_url="http://test/api/v1",
        ) as client:
            yield client

    finally:
        app.dependency_overrides.pop(get_async_session, None)
