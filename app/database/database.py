from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from databases import Database

from app.core.config import POSTGRES_STR_FOR_CONNECT
from app.database.models import Base


# URL для PostgreSQL
database = Database(POSTGRES_STR_FOR_CONNECT)

engine = create_async_engine(POSTGRES_STR_FOR_CONNECT, echo=True)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def init_models():
    async with engine.begin() as conn:
        # await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


# Dependency
async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session
