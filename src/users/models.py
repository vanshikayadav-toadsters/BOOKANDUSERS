from sqlmodel import SQLModel, Field, Column
import uuid
import sqlalchemy.dialects.postgresql as pg
from datetime import datetime


class User(SQLModel, table=True):
    __tablename__ = "users"

    uid: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(pg.UUID(as_uuid=True), primary_key=True, unique=True, nullable=False)
    )

    username: str = Field(unique=True, index=True)
    first_name: str | None = None
    last_name: str | None = None
    is_verified: bool = False
    email: str = Field(unique=True, index=True)

    password_hash: str = Field(nullable=False)

    created_at: datetime = Field(
        default_factory=datetime.utcnow,
        sa_column=Column(pg.TIMESTAMP, nullable=False)
    )

    def __repr__(self) -> str:
        return f"<User {self.username}>"
