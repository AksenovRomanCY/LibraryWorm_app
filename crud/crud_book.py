from sqlalchemy.orm import Session
import uuid

import models as model
from schemas import schema_book as schema


def get_book_by_name(db: Session, book_name: str):
    return db.query(model.Books).filter(model.Books.book_name == book_name).first()


def get_book_by_library_id(db: Session, library_id: str):
    return db.query(model.Books).filter(model.Books.library_id == library_id).first()


def get_books(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.Books).offset(skip).limit(limit).all()


def create_book(db: Session, data: schema.BookCreate):  # UserCreate
    db_user = model.Books(book_name=data.book_name, library_id=data.library_id, book_uid=uuid.uuid4())
    try:
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
    except Exception as e:
        print(e)
    return db_user


def update_book_by_library_id(db: Session, library_id: str, data: schema.BookBase):
    db_user = db.query(model.Books).filter(model.Books.library_id == library_id).first()
    db_user.book_name = data.book_name
    db_user.book_author = data.book_author
    db_user.book_description = data.book_description
    try:
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
    except Exception as e:
        print(e)
    return db_user


def update_student_in_book_by_library_id(db: Session, library_id: str, student_name: str):
    db_user = db.query(model.Books).filter(model.Books.library_id == library_id).first()
    db_user_st = db.query(model.Students).filter(model.Books.student_name == student_name).first()
    db_user.student_uid = db_user_st.student_uid
    try:
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
    except Exception as e:
        print(e)
    return db_user
