from fastapi import FastAPI
from sqlmodel import SQLModel
from src.db.main import engine
from src.users.routes import router as users_router
from src.books.routes import router as books_router

app = FastAPI()

@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)

app.include_router(users_router)
app.include_router(books_router)
