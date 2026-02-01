from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.main import get_session
from src.books.service import BookService
from src.books.schemas import BookCreate, BookRead

router = APIRouter(prefix="/books", tags=["Books"])
service = BookService()

@router.post("/", response_model=BookRead)
async def create_book(
    data: BookCreate,
    session: AsyncSession = Depends(get_session)
):
    return await service.create_book(session, data)

@router.get("/", response_model=list[BookRead])
async def get_books(
    session: AsyncSession = Depends(get_session)
):
    return await service.get_books(session)
