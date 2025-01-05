from pydantic import BaseModel


class UserCreate(BaseModel):
    """ Модель UserCreate для регистрации """
    username: str
    password: str


class CurrencyList(BaseModel):
    """ Модель CurrencyList для отображения списка поддерживаемых валют и их кодов """
    base: str
    list_code: str


class CurrencyConvert(BaseModel):
    """ Модель CurrencyConvert для конвертации валюты """
    to_code: str
    from_code: str
    amount: int
