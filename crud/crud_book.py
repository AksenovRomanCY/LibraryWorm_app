from sqlalchemy.orm import Session
import uuid
import time

import models as model
from schemas import schema_book as schema


def get_book_by_name(db: Session, book_name: str):
    db_users = db.query(
        model.Books.book_name, model.Books.book_author_surname, model.Books.book_author, model.Books.book_description,
        model.Books.available, model.Books.library_id, model.Books.language, model.Books.school,
        model.Books.date_of_issue, model.Students.student_surname, model.Students.student_name,
        model.Students.student_class)
    return db_users.join(model.Students).filter(model.Books.book_name == book_name).first()


def get_book_by_library_id(db: Session, library_id: str):
    db_users = db.query(
        model.Books.book_name, model.Books.book_author_surname, model.Books.book_author, model.Books.book_description,
        model.Books.available, model.Books.library_id, model.Books.language, model.Books.school,
        model.Books.date_of_issue, model.Students.student_surname, model.Students.student_name,
        model.Students.student_class)
    return db_users.join(model.Students).filter(model.Books.library_id == library_id).first()


def create_book(db: Session, data: schema.BookCreate):
    db_user = model.Books(
        book_name=data.book_name, book_author_surname=data.book_author_surname, book_author=data.book_author,
        book_description=data.book_description, library_id=data.library_id, school=data.school,
        language=data.language, book_uid=uuid.uuid4())
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
    db_user.book_author_surname = data.book_author_surname
    db_user.book_author = data.book_author
    db_user.book_description = data.book_description
    db_user.school = data.school
    try:
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
    except Exception as e:
        print(e)
    return db_user


def add_student_in_book_by_library_id(db: Session, library_id: str, student_name: str):
    db_user = db.query(model.Books).filter(model.Books.library_id == library_id).first()
    db_user_st = db.query(model.Students).filter(model.Students.student_name == student_name).first()
    db_user.student_uid = db_user_st.student_uid
    db_user.available = False
    current_time = time.time()
    local_time = time.localtime(current_time)
    db_user.date_of_issue = time.strftime("%d-%m-%Y", local_time)
    try:
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
    except Exception as e:
        print(e)
    return db_user


def remove_student_in_book_by_library_id(db: Session, library_id: str):
    db_user = db.query(model.Books).filter(model.Books.library_id == library_id).first()
    db_user.student_uid = uuid.UUID(int=0)
    db_user.available = True
    db_user.date_of_issue = '00-00-0000'
    try:
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
    except Exception as e:
        print(e)
    return db_user


def get_books_all(db: Session, skip: int = 0, limit: int = 100):
    db_users = db.query(
        model.Books.book_name, model.Books.book_author_surname, model.Books.book_author, model.Books.book_description,
        model.Books.available, model.Books.library_id, model.Books.language, model.Books.school,
        model.Books.date_of_issue, model.Students.student_surname, model.Students.student_name,
        model.Students.student_class)
    return db_users.join(model.Students).offset(skip).limit(limit).all()
