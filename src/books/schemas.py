from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class BookCreate(BaseModel):
    title: str
    author: str


class BookRead(BaseModel):
    id: UUID
    title: str
    author: str
    owner_id: UUID
    created_at: datetime

    class Config:
        from_attributes = True
