from fastapi import FastAPI
from sqlmodel import SQLModel
from contextlib import asynccontextmanager

from src.db.main import engine
from src.users.routes import router as users_router
from src.books.routes import router as books_router
from src.auth.routes import auth_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)

    yield


app = FastAPI(lifespan=lifespan)

app.include_router(auth_router)
app.include_router(users_router)
app.include_router(books_router)
