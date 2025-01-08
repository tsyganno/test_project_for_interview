from fastapi import HTTPException
from httpx import AsyncClient


class CurrencyAPI:
    def __init__(self, api_key: str, base_url: str):
        self.api_key = api_key
        self.base_url = base_url
        self.headers = {"apikey": self.api_key}

    async def _make_request(self, endpoint: str, params: dict):
        async with AsyncClient() as client:
            response = await client.get(f"{self.base_url}{endpoint}", params=params, headers=self.headers)
            # Проверяем успешность запроса через not
            if not response.status_code == 200:
                raise HTTPException(
                    status_code=response.status_code,
                    detail=response.json().get("Error", "An error occurred while accessing the currency API.")  # тут мы прикидываем полученную ошибку выше (и статус код, и содержание ошибки)
                )

            return response.json()

    async def get_list(self, base: str, symbols: str):
        return await self._make_request("", {"base": base, "symbols": symbols})

    async def get_convert(self, to_code: str, from_code: str, amount: float):
        return await self._make_request("convert", {"to": to_code, "from": from_code, "amount": amount})