from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.users.models import User
from src.users.schemas import UserCreate

class UserService:
    
    async def create_user(self, session: AsyncSession, data: UserCreate):
        user = User(**data.model_dump())
        session.add(user)
        await session.commit()
        await session.refresh(user)
        return user
    
    async def get_users(self, session: AsyncSession):
        result = await session.execute(select(User))
        return result.scalars().all()
