from pydantic import BaseModel


class UserCreate(BaseModel):
    """ Модель UserCreate для регистрации """
    username: str
    password: str
