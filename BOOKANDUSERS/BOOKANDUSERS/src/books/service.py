from sqlmodel import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.books.models import Book
from src.books.schemas import BookCreate

class BookService:
    
    async def create_book(self, session:AsyncSession, data: BookCreate):
        book=Book(**data.model_dump())
        session.add(book)
        await session.commit()
        await session.refresh(book)
        return book
    
    async def get_books(self,session:AsyncSession):
        result=await session.exec(select(Book))
        return result.all_()