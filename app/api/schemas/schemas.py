from pydantic import BaseModel


class UserCreate(BaseModel):
    """ Модель UserCreate для ркгистрации """
    username: str
    password: str
