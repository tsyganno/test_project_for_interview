from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordRequestForm # для реквест-формы нам нужно установить доп. библиотеку командой pip install python-multipart
from typing import Annotated

from app.core.security import create_jwt_token, get_user, get_user_from_token
from app.api.schemas.schemas import UserCreate
from app.database.database import USERS_DATA

user_router = APIRouter()


# Роут для получения JWT-токена (так работает логин)
@user_router.post('/auth/login/')
def login(user_data: Annotated[OAuth2PasswordRequestForm, Depends()]):  # тут логинимся через форму
    user_data_from_db = get_user(user_data.username)
    if user_data_from_db is None or user_data.password != user_data_from_db['password']:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return {"access_token": create_jwt_token({"sub": user_data.username})}  # тут мы добавляем полезную нагрузку в токен, и говорим, что "sub" содержит значение username


@user_router.post('/auth/register/')
def create_new_user(user: UserCreate):
    new_user = {"username": user.username, "password": user.password}
    if new_user in USERS_DATA:
        return {"message": "Error! User already exists"}
    USERS_DATA.append(new_user)
    return {"message": "User successfully created", "username": user.username, "password": user.password}


