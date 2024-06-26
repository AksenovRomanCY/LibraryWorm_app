from sqlalchemy.orm import Session
import uuid
import time
from sqlalchemy import func

import models as model
from schemas import schema_book as schema


def get_book_by_name(db: Session, book_name: str):
    db_book = db.query(
        model.Books.book_name, model.Books.book_author_surname, model.Books.book_author, model.Books.book_description,
        model.Books.available, model.Books.library_id, model.Books.language, model.Books.school,
        model.Books.date_of_issue, model.Students.student_surname, model.Students.student_name,
        model.Students.student_class)
    return db_book.join(model.Students).filter(model.Books.book_name == book_name).first()


def get_book_by_library_id(db: Session, library_id: str):
    db_book = db.query(
        model.Books.book_name, model.Books.book_author_surname, model.Books.book_author, model.Books.book_description,
        model.Books.available, model.Books.library_id, model.Books.language, model.Books.school,
        model.Books.date_of_issue, model.Students.student_surname, model.Students.student_name,
        model.Students.student_class)
    return db_book.join(model.Students).filter(model.Books.library_id == library_id).first()


def create_book(db: Session, data: schema.BookCreate):
    db_book = model.Books(
        book_name=data.book_name, book_author_surname=data.book_author_surname, book_author=data.book_author,
        book_description=data.book_description, library_id=data.library_id, school=data.school,
        language=data.language, book_uid=uuid.uuid4())
    try:
        db.add(db_book)
        db.commit()
        db.refresh(db_book)
    except Exception as e:
        print(e)
    return db_book


def update_book_by_library_id(db: Session, library_id: str, data: schema.BookBase):
    db_book = db.query(model.Books).filter(model.Books.library_id == library_id).first()
    db_book.book_name = data.book_name
    db_book.book_author_surname = data.book_author_surname
    db_book.book_author = data.book_author
    db_book.book_description = data.book_description
    db_book.school = data.school
    try:
        db.add(db_book)
        db.commit()
        db.refresh(db_book)
    except Exception as e:
        print(e)
    return db_book


def add_student_in_book_by_library_id(db: Session, library_id: str, student_surname: str, student_name: str, date: str):
    db_book = db.query(model.Books).filter(model.Books.library_id == library_id).first()
    db_book_st = db.query(model.Students).filter(model.Students.student_name == student_name,
                                                 model.Students.student_surname == student_surname).first()
    db_book.student_uid = db_book_st.student_uid
    db_book.available = False
    if date == 'current':
        current_time = time.time()
        local_time = time.localtime(current_time)
        db_book.date_of_issue = time.strftime("%Y-%m-%d", local_time)
    else:
        db_book.date_of_issue = date
    try:
        db.add(db_book)
        db.commit()
        db.refresh(db_book)
    except Exception as e:
        print(e)
    return db_book


def remove_student_in_book_by_library_id(db: Session, library_id: str):
    db_book = db.query(model.Books).filter(model.Books.library_id == library_id).first()
    db_book.student_uid = uuid.UUID(int=0)
    db_book.available = True
    db_book.date_of_issue = '0000-00-00'
    try:
        db.add(db_book)
        db.commit()
        db.refresh(db_book)
    except Exception as e:
        print(e)
    return db_book


def get_books_all(db: Session):
    db_books = db.query(
        model.Books.book_name, model.Books.book_author_surname, model.Books.book_author, model.Books.book_description,
        model.Books.available, model.Books.library_id, model.Books.language, model.Books.school,
        model.Books.date_of_issue, model.Students.student_surname, model.Students.student_name,
        model.Students.student_class)
    return db_books.join(model.Students).all()


def get_number_of_book(db: Session):
    return db.query(func.count()).select_from(model.Books).scalar()


def remove_book(db: Session, library_id: str):
    db_book = db.query(model.Books).filter(model.Books.library_id == library_id).first()
    try:
        db.delete(db_book)
        db.commit()
        db.refresh(db_book)
    except Exception as e:
        print(e)
    return db_book
