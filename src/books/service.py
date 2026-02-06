from sqlmodel import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.books.models import Book
from src.books.schemas import BookCreate
from src.users.models import User

class BookService:
    
    async def create_book(self, session: AsyncSession, data: BookCreate, user: User) -> Book:
        book = Book(
            title=data.title,
            author=data.author,
            owner_id=user.uid
        )

        session.add(book)
        await session.commit()
        await session.refresh(book)
        return book
    
    async def get_books(self, session: AsyncSession) -> list[Book]:
        result = await session.exec(select(Book))
        return result.all()
