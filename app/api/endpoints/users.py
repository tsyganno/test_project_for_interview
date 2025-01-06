from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm # для реквест-формы нам нужно установить доп. библиотеку командой pip install python-multipart
from typing import Annotated

from app.core.security import create_jwt_token, get_user
from app.api.schemas.schemas import UserCreate
from app.database.crud import *
from app.api.exception_handlers.exception_handlers import UserExists, UserNotFoundException


user_router = APIRouter()


@user_router.post('/auth/login/')
async def login(user_data: Annotated[OAuth2PasswordRequestForm, Depends()]):  # тут логинимся через форму
    """ Роут для получения JWT-токена (так работает логин) """
    user_data_from_db = await get_user(user_data.username)
    if user_data_from_db:
        if user_data_from_db.username_user is None or user_data.password != user_data_from_db.password_user:
            raise UserNotFoundException()
        return {"access_token": await create_jwt_token({"sub": user_data.username})}  # тут мы добавляем полезную нагрузку в токен, и говорим, что "sub" содержит значение username
    else:
        raise UserNotFoundException()


@user_router.post('/auth/register/')
async def create_new_user(user: UserCreate):
    """ Роут для регистрации пользователя """
    user_db = await search_user_in_the_database(user.username)
    if user_db:
        raise UserExists()
    await write_user_to_the_database(user.username, user.password)
    return {"message": "User successfully created",
            "username": user.username,
            "password": user.password}
