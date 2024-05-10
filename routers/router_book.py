from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db

from crud import crud_book as crud
from schemas import schema_book as schema

router = APIRouter()


@router.post('/books/', response_model=schema.BookCreate)
def create_book(data: schema.BookCreate = None, db: Session = Depends(get_db)):  # UserCreate
    db_user = crud.get_book_by_lib_id(db, library_id=data.library_id)
    if db_user:
        raise HTTPException(status_code=400, detail="Book already registered")
    return crud.create_book(db=db, data=data)


@router.get("/books/", response_model=list[schema.BookBase])
def read_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_books(db, skip=skip, limit=limit)


@router.get("/books/", response_model=list[schema.BookBase])
def read_books_plus_name(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_books(db, skip=skip, limit=limit)


@router.get("/books/{str(book_uid)}", response_model=schema.BookBase)
def read_book_by_uid(book_uid: str = None, db: Session = Depends(get_db)):
    db_user = crud.get_book_by_uid(db, book_uid=book_uid)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.get("/books/{str(book_name)}", response_model=schema.BookBase)
def get_user_by_name(book_name: str = None, db: Session = Depends(get_db)):
    db_user = crud.get_book_by_name(db, book_name=book_name)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.get("/books/{str(library_id)}", response_model=schema.BookBase)
def get_user_by_lib_id(library_id: str = None, db: Session = Depends(get_db)):
    db_user = crud.get_book_by_lib_id(db, library_id=library_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.put("/books/{str(book_uid)}", response_model=schema.BookBase)
def update_user_by_id(data: schema.BookBase = None, book_uid: str = None, db: Session = Depends(get_db)):
    db_user = crud.get_book_by_uid(db, book_uid=book_uid)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.update_book_by_uid(data=data, db=db, book_uid=book_uid)


@router.put("/books/{str(book_uid)}/{str(student_name)}", response_model=schema.BookStudentAppend)
def update_student_in_book_by_uid(book_uid: str = None,student_name: str = None, db: Session = Depends(get_db)):
    db_user = crud.get_book_by_uid(db, book_uid=book_uid)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.update_student_in_book_by_uid(student_name=student_name, db=db, book_uid=book_uid)