from sqlalchemy import select
from sqlalchemy import update, delete

from app.database.models import User
from app.database.database import async_session


async def write_user_to_the_database(username: str, password: str):
    """ Запись пользователя в таблицу User в БД """
    async with async_session() as session:
        query = User(username_user=username, password_user=password)
        session.add(query)
        await session.commit()


async def search_user_in_the_database(username: str):
    """ Поиск пользователя по username в таблице User в БД """
    async with async_session() as session:
        user_query_id = select(User).where(User.username_user == username)
        user_result_id = await session.execute(user_query_id)
        user = user_result_id.scalars().first()  # Возвращает одного пользователя или None
        return user
