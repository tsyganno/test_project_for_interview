from fastapi import APIRouter, Depends
from typing import Annotated

from app.utils.external_api import CurrencyAPI
from app.core.security import get_user, get_user_from_token
from app.api.exception_handlers.exception_handlers import UserNotFoundException
from app.core.config import EXTERNAL_CURRENCY_URL_ROUTE, API_KEY_CURRENCY, EXTERNAL_CONVERT_CURRENCY_URL_ROUTE


currency_router = APIRouter(prefix="/currency")


@currency_router.get("/list/")
async def currency_list(base: str, list_code: str, current_user: Annotated[str, Depends(get_user_from_token)]):
    """ Роут для получения списка поддерживаемых валют и их кодов """
    user = await get_user(current_user)
    if not user:
        raise UserNotFoundException()
    curr_list = CurrencyAPI(API_KEY_CURRENCY, EXTERNAL_CURRENCY_URL_ROUTE)
    return await curr_list.get_list(base, list_code)


@currency_router.get("/exchange/")
async def convert_currency(from_code: str, to_code: str, amount: float, current_user: Annotated[str, Depends(get_user_from_token)]):
    """ Роут для получения конвертируемой валюты """
    user = await get_user(current_user)
    if not user:
        raise UserNotFoundException()
    curr_convert = CurrencyAPI(API_KEY_CURRENCY, EXTERNAL_CONVERT_CURRENCY_URL_ROUTE)
    return await curr_convert.get_convert(to_code, from_code, amount)
