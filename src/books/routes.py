from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.main import get_session
from src.books.service import BookService
from src.books.schemas import BookCreate, BookRead
from src.auth.dependencies import get_current_user
from src.users.models import User

router = APIRouter(prefix="/books", tags=["Books"])
service = BookService()


@router.post("/", response_model=BookRead, status_code=status.HTTP_201_CREATED)
async def create_book(
    data: BookCreate,
    session: AsyncSession = Depends(get_session),
    current_user: User = Depends(get_current_user)
):
    try:
        return await service.create_book(session, data, current_user)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create book"
        )


@router.get("/", response_model=list[BookRead])
async def get_books(
    session: AsyncSession = Depends(get_session)
):
    return await service.get_books(session)
