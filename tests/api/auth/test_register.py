import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_register_password_missmatch(async_client: AsyncClient) -> None:
    response = await async_client.post(
        "/auth/register",
        json={
            "email": "shailesh@gmail.com",
            "password": "shailesh@12345",
            "confirm_password": "shailesh@12",
        },
    )

    assert response.status_code == 400


@pytest.mark.asyncio
async def test_register_success(async_client: AsyncClient) -> None:
    response = await async_client.post(
        "/auth/register",
        json={
            "email": "shailesh@gmail.com",
            "password": "shailesh@12345",
            "confirm_password": "shailesh@12345",
        },
    )

    assert response.status_code == 200


@pytest.mark.asyncio
async def test_register_email_exists(async_client: AsyncClient) -> None:
    response = await async_client.post(
        "/auth/register",
        json={
            "email": "shailesh@gmail.com",
            "password": "shailesh@12345",
            "confirm_password": "shailesh@12345",
        },
    )

    assert response.status_code == 409
