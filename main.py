import uvicorn
import asyncio
import time
from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.responses import JSONResponse

from app.api.endpoints.users import user_router
from app.api.endpoints.currency import currency_router
from app.database.database import database, init_models

from app.api.exception_handlers.exception_handlers import UserExists, UserNotFoundException


@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    yield
    await database.disconnect()


app = FastAPI()
app.include_router(user_router)
app.include_router(currency_router)


@app.exception_handler(UserExists)
async def user_exists(request, exc):
    start_time = time.time()
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
        headers={'X-ErrorHandleTime': str(time.time() - start_time)}
    )


@app.exception_handler(UserNotFoundException)
async def user_not_found_exception_handler(request, exc):
    start_time = time.time()
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
        headers={'X-ErrorHandleTime': str(time.time() - start_time)}
    )


if __name__ == '__main__':
    asyncio.run(init_models())
    uvicorn.run(
        "main:app",
        host='localhost',
        port=8000,
        reload=True
    )
