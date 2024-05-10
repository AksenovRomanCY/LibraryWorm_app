from sqlalchemy.orm import Session

import models as model
from schemas import schema_book as schema


def get_book_by_id(db: Session, book_uid: str):
    return db.query(model.Books).filter(model.Books.book_uid == book_uid).first()


def get_book_by_name(db: Session, book_name: str):
    return db.query(model.Books).filter(model.Books.book_name == book_name).first()


def get_books(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.Books).offset(skip).limit(limit).all()


def create_book(db: Session, data: schema.BookCreate):  # UserCreate
    db_user = model.Books(book_name=data.book_name, library_id=data.library_id)
    try:
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
    except Exception as e:
        print(e)
    return db_user


def update_book_by_id(db: Session, book_uid: str, data: schema.BookBase):
    db_user = db.query(model.Books).filter(model.Books.book_uid == book_uid).first()
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


def update_student_in_book(db: Session, book_uid: str, student_uid: str):
    db_user = db.query(model.Books).filter(model.Books.book_uid == book_uid).first()
    db_user.student_uid = student_uid
    try:
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
    except Exception as e:
        print(e)
    return db_user


