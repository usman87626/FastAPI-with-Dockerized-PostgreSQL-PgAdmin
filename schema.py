from pydantic import BaseModel

class Book(BaseModel):
    __tablename__ = "book"
    title: str
    rating: int
    author_id: int
    
    class Config:
        orm_mode = True

class Author(BaseModel):
    name: str
    age: int
    class Config:
        orm_mode = True