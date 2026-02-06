from pydantic import BaseModel, EmailStr
from uuid import UUID
from datetime import datetime

class UserCreate(BaseModel):
    first_name: str
    last_name: str
    username: str
    email: EmailStr
    password: str


class UserRead(BaseModel):
    uid: UUID
    username: str
    first_name: str | None = None
    last_name: str | None = None
    is_verified: bool = False
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True


class UserUpdate(BaseModel):
    username: str | None = None
    email: EmailStr | None = None
