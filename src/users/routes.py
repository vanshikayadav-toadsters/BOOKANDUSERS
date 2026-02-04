from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.main import get_session
from src.users.service import UserService
from src.users.schemas import UserCreate, UserRead

router = APIRouter(prefix="/users", tags=["Users"])
service = UserService()

@router.post("/" , response_model = UserRead)
async def create_user(
    data: UserCreate,
    session: AsyncSession = Depends(get_session)
):
    return await service.create_user(session , data)


@router.get("/", response_model=list[UserRead])
async def get_users(
    session: AsyncSession = Depends(get_session)
):
    return await service.get_users(session)