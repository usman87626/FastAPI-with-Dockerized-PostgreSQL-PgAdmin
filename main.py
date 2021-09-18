import uvicorn
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware, db
import os
from dotenv import load_dotenv
#Import DB Schema
from schema import Book as SchemaBook
from schema import Author as SchemaAuthor
# IMPORT MODELS
from models import Book 
from models import Author 
load_dotenv(".env")

app = FastAPI()

app.add_middleware(DBSessionMiddleware,db_url=os.environ["DATABASE_URL"])

@app.get("/")
async def root():
    return {"Message":"Hello FAST API"} 

@app.post("/add-book/",response_model=SchemaBook)
def add_book(book: SchemaBook):
    db_book = Book(title=book.title,rating=book.rating,author_id=book.author_id)
    db.session.add(db_book)
    db.session.commit()
    return db_book

@app.post("/add-author/",response_model=SchemaAuthor)
def add_author(author: SchemaAuthor):
    db_author = Author(name=author.name,age=author.age)
    db.session.add(db_author)
    db.session.commit()
    return db_author

@app.get("/books/")
def get_books():
    books = db.session.query(Book).all()
    return books

@app.get("/authors/")
def get_authors():
    authors = db.session.query(Author).all()
    return authors
    