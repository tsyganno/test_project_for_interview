import requests
from fastapi import HTTPException


from app.core.config import EXTERNAL_CURRENCY_URL_ROUTE, API_KEY_CURRENCY, EXTERNAL_CONVERT_CURRENCY_URL_ROUTE
from app.api.schemas.schemas import CurrencyConvert, CurrencyList


async def get_list(currency_list: CurrencyList):
    """ Функция с запросом API для получения списка поддерживаемых валют и их кодов """
    response = requests.get(EXTERNAL_CURRENCY_URL_ROUTE,
                            params={"base": currency_list.base, "symbols": currency_list.list_code},
                            headers={"apikey": API_KEY_CURRENCY}
                            )
    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status_code=400, detail="Bad currency code")


async def get_convert(currency_convert: CurrencyConvert):
    """ Функция с запросом API для получения конвертируемой валюты """
    response = requests.get(EXTERNAL_CONVERT_CURRENCY_URL_ROUTE + "convert",
                            params={
                                "to": currency_convert.to_code,
                                "from": currency_convert.from_code,
                                "amount": currency_convert.amount},
                            headers={"apikey": API_KEY_CURRENCY}
                            )
    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status_code=400, detail="Bad currency code")
