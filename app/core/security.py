import jwt  # Тут работаем с библиотекой PyJWT

from datetime import datetime
from fastapi import HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer # для реквест-формы нам нужно установить доп. библиотеку командой pip install python-multipart

from app.core.config import SECRET_KEY, ALGORITHM, EXPIRATION_TIME
from app.database.crud import *


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login/") # OAuth2PasswordBearer для авторизации по токену


async def create_jwt_token(data: dict):
    """ Функция для создания JWT токена с полезной нагрузкой"""
    data.update({"exp": datetime.utcnow() + EXPIRATION_TIME})
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)  # кодируем токен, передавая в него наш словарь с тем, что мы хотим там разместить


async def get_user_from_token(token: str = Depends(oauth2_scheme)):
    """ Функция по извлечению информации о пользователе из полезной нагрузки """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])  # декодируем токен
        return payload.get("sub") # тут мы идем в полезную нагрузку JWT-токена и возвращаем утверждение о юзере (subject); обычно там еще можно взять "iss" - issuer/эмитент, или "exp" - expiration time - время 'сгорания' и другое, что мы сами туда кладем
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token has expired",
            headers={"WWW-Authenticate": "Bearer"},
        )
    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"},
        )


async def get_user(username: str):
    """ Функция для получения пользовательских данных на основе имени пользователя """
    user = await search_user_in_the_database(username)
    return user
