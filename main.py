import uvicorn
import asyncio
from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.api.endpoints.users import user_router
from app.api.endpoints.currency import currency_router
from app.database.database import database, init_models


@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    yield
    await database.disconnect()


app = FastAPI()
app.include_router(user_router)
app.include_router(currency_router)


if __name__ == '__main__':
    asyncio.run(init_models())
    uvicorn.run(
        "main:app",
        host='localhost',
        port=8000,
        reload=True
    )
