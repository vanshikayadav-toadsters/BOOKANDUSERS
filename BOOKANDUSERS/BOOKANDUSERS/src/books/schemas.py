from pydantic import BaseModel
from uuid import UUID


class BookCreate(BaseModel):
    title:str
    author:str
    owner_id:UUID
    
class BookRead(BaseModel):
    id:UUID
    title:str
    author:str
    owner_id:UUID
    
    