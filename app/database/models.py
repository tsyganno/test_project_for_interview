from sqlalchemy import Column, String, BigInteger
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class User(Base):
    """ Таблица User в БД """
    __tablename__ = "users"

    id = Column(BigInteger, autoincrement=True, primary_key=True, index=True)
    username_user = Column(String)
    password_user = Column(String)
