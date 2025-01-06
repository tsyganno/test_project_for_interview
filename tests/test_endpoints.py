import pytest
from main import app
from httpx import ASGITransport
from httpx import AsyncClient


# Тесты для эндпоинтов модуля users.py

@pytest.mark.asyncio
async def test_register_user_success():
    async with AsyncClient(transport=ASGITransport(app), base_url="http://test") as client:
        response = await client.post("/auth/register/", json={"username": "newuser", "password": "password12322"})
    assert response.status_code == 200
    assert response.json()["message"] == "User successfully created."
    assert response.json()["username"] == "newuser"


@pytest.mark.asyncio
async def test_register_existing_user():
    async with AsyncClient(transport=ASGITransport(app), base_url="http://test") as client:
        response = await client.post("/auth/register/", json={"username": "dimon", "password": "123"})
    assert response.status_code == 400
    assert response.json()["detail"] == "Error! User already exists."


@pytest.mark.asyncio
async def test_login_success():
    async with AsyncClient(transport=ASGITransport(app), base_url="http://test") as client:
        response = await client.post("/auth/login/", data={"username": "dimon", "password": "123"})
    assert response.status_code == 200
    response_data = response.json()
    assert "access_token" in response_data
    return response.json()["access_token"]


@pytest.mark.asyncio
async def test_login_invalid_credentials():
    async with AsyncClient(transport=ASGITransport(app), base_url="http://test") as client:
        response = await client.post("/auth/login/", data={"username": "dimon", "password": "wrongpassword"})
    assert response.status_code == 400
    assert response.json()["detail"] == "Error! The user was not found."


@pytest.mark.asyncio
async def test_login_user_not_exists():
    async with AsyncClient(transport=ASGITransport(app), base_url="http://test") as client:
        response = await client.post("/auth/login/", data={"username": "unknownuser", "password": "password"})
    assert response.status_code == 400
    assert response.json()["detail"] == "Error! The user was not found."


# Тесты для эндпоинтов модуля currency.py

@pytest.mark.asyncio
async def test_currency_list_success():
    token = await test_login_success()
    async with AsyncClient(transport=ASGITransport(app), base_url="http://test") as client:
        response = await client.get("/currency/list/", params={"base": "usd", "list_code": "usd"}, headers={"Authorization": F"Bearer {token}"})
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_currency_list_failure_invalid_token():
    token = await test_login_success() + 'aa13'
    async with AsyncClient(transport=ASGITransport(app), base_url="http://test") as client:
        response = await client.get("/currency/list/", params={"base": "usd", "list_code": "eur"}, headers={"Authorization": F"Bearer {token}"})
    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid token"


@pytest.mark.asyncio
async def test_convert_currency_success():
    token = await test_login_success()
    async with AsyncClient(transport=ASGITransport(app), base_url="http://test") as client:
        response = await client.get("/currency/exchange/", params={"to_code": "eur", "from_code": "usd", "amount": "100"}, headers={"Authorization": F"Bearer {token}"})
        assert response.status_code == 200


@pytest.mark.asyncio
async def test_convert_currency_failure():
    token = await test_login_success()
    async with AsyncClient(transport=ASGITransport(app), base_url="http://test") as client:
        response = await client.get("/currency/exchange/", params={"from_code": "wqq", "to_code": "eur", "amount": "100"}, headers={"Authorization": F"Bearer {token}"})
        assert response.status_code == 400
        assert response.json()["detail"] == "Bad currency code"


@pytest.mark.asyncio
async def test_convert_currency_failure_invalid_token():
    token = await test_login_success() + '2fc'
    async with AsyncClient(transport=ASGITransport(app), base_url="http://test") as client:
        response = await client.get("/currency/exchange/", params={"from_code": "usd", "to_code": "eur", "amount": "100"}, headers={"Authorization": F"Bearer {token}"})
        assert response.status_code == 401
        assert response.json()["detail"] == "Invalid token"


# pytest tests/
