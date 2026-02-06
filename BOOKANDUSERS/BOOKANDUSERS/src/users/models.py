from sqlmodel import SQLModel , Field
from uuid import UUID , uuid4
from datetime import datetime

class User(SQLModel , table=True):
    __tablename__ = "users"
    
    id: UUID=Field(default_factory=uuid4, primary_key=True)
    username:str
    email:str
    password:str
    
    created_at: datetime = Field(default_factory = datetime.utcnow)
    