from pydantic import BaseModel, EmailStr
from uuid import UUID

class UserCreate(BaseModel):
    username:str
    email:EmailStr
    password:str
    
class UserRead(BaseModel):
    id:UUID
    username:str
    email:EmailStr
    
class UserUpdate(BaseModel):
    username:str |None=None
    email:EmailStr | None = None
    