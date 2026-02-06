from sqlmodel import SQLModel, Field, Column
from uuid import UUID, uuid4
from datetime import datetime
from typing import Optional
import sqlalchemy.dialects.postgresql as pg

class Book(SQLModel, table= True):
    __tablename__="books"
    
    id:UUID = Field(default_factory=uuid4 , primary_key=True)
    title:str
    author:str
    owner_id: UUID = Field(foreign_key="users.uid", nullable=False)
    created_at: datetime = Field(
        default_factory=datetime.utcnow,
        sa_column=Column(pg.TIMESTAMP, nullable=False)
    )

    
