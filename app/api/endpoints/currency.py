from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated

from app.utils.external_api import get_list, get_convert, CurrencyConvert, CurrencyList
from app.core.security import get_user, get_user_from_token

currency_router = APIRouter()


@currency_router.get("/currency/list/")
async def currency_list(base: str, list_code: str, current_user: Annotated[str, Depends(get_user_from_token)]):
    user = await get_user(current_user)
    if user is None:
        raise HTTPException(
            status_code=403,
            detail="Not authorized"
        )
    return await get_list(CurrencyList(base=base, list_code=list_code))


@currency_router.get("/currency/exchange/")
async def convert_currency(from_code: str, to_code: str, amount: str, current_user: Annotated[str, Depends(get_user_from_token)]):
    user = await get_user(current_user)
    if user is None:
        raise HTTPException(
            status_code=403,
            detail="Not authorized"
        )
    return await get_convert(
        CurrencyConvert(
            to_code=to_code,
            from_code=from_code,
            amount=amount)
    )
