from sqlmodel import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from src.users.models import User
from src.users.schemas import UserCreate
from src.auth.utils import generate_password_hash

class UserService:
    
    async def create_user(self, session: AsyncSession, data: UserCreate) -> User:
        user_data = data.model_dump()
        user_data["password_hash"] = generate_password_hash(user_data.pop("password"))
        user = User(**user_data)
        session.add(user)
        await session.commit()
        await session.refresh(user)
        return user
    
    async def get_users(self, session: AsyncSession) -> list[User]:
        result = await session.exec(select(User))
        return result.all()
