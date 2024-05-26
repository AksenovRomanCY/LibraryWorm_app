from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db

from crud import crud_book as crud
from schemas import schema_book as schema

router = APIRouter()


@router.post('/create_book/', response_model=schema.BookCreate)
def create_book(data: schema.BookCreate = None, db: Session = Depends(get_db)):
    db_user = crud.get_book_by_library_id(db, library_id=data.library_id)
    if db_user:
        raise HTTPException(status_code=400, detail="Book already registered")
    return crud.create_book(db=db, data=data)


@router.get("/get_book_list/", response_model=list[schema.BookSee])
def get_books_all(db: Session = Depends(get_db)):
    return crud.get_books_all(db)


@router.get("/get_book_name/{str(book_name)}", response_model=schema.BookSee)
def get_book_by_name(book_name: str = None, db: Session = Depends(get_db)):
    db_user = crud.get_book_by_name(db, book_name=book_name)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_user


@router.get("/get_book_id/{str(library_id)}", response_model=schema.BookSee)
def get_book_by_library_id(library_id: str = None, db: Session = Depends(get_db)):
    db_user = crud.get_book_by_library_id(db, library_id=library_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_user


@router.put("/update/{str(library_id)}", response_model=schema.BookBase)
def update_book_by_library_id(data: schema.BookBase = None, library_id: str = None, db: Session = Depends(get_db)):
    db_user = crud.get_book_by_library_id(db, library_id=library_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.update_book_by_library_id(data=data, db=db, library_id=library_id)


@router.put("/update_a/{str(library_id)}/{str(student_name)}/{str(date)}", response_model=schema.BookBase)
def add_student_in_book_by_library_id(
        library_id: str = None, student_name: str = None, date: str = None, db: Session = Depends(get_db)):
    db_user = crud.get_book_by_library_id(db, library_id=library_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return crud.add_student_in_book_by_library_id(student_name=student_name, db=db, library_id=library_id, date=date)


@router.put("/update_r/{str(library_id)}", response_model=schema.BookBase)
def remove_student_in_book_by_library_id(
        library_id: str = None, db: Session = Depends(get_db)):
    return crud.remove_student_in_book_by_library_id(db=db, library_id=library_id)
