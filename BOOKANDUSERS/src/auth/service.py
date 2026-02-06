from src.users.models import User
from .schemas import UserCreate
from .utils import generate_password_hash
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select
from typing import Optional


class UserService:
    async def get_user_by_email(self, email: str, session: AsyncSession) -> Optional[User]:
        statement = select(User).where(User.email == email)
        result = await session.execute(statement)
        user = result.scalars().first()
        return user

    async def user_exists(self, email: str, session: AsyncSession) -> bool:
        user = await self.get_user_by_email(email, session)
        return True if user is not None else False

    async def create_user(self, session: AsyncSession, user_data: UserCreate) -> User:
        # Check if user already exists
        existing_user = await self.get_user_by_email(user_data.email, session)
        if existing_user:
            raise ValueError("User with this email already exists")
        
        user_data_dict = user_data.model_dump()
        password = user_data_dict.pop("password")
        user_data_dict["password_hash"] = generate_password_hash(password)

        new_user = User(**user_data_dict)

        session.add(new_user)
        await session.commit()
        await session.refresh(new_user)

        return new_user
