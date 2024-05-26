from sqlalchemy.orm import Session
import uuid

import models as model
from schemas import schema_student as schema


def get_student_by_name(db: Session, student_name: str):
    return db.query(model.Students).filter(model.Students.student_name == student_name).first()


def get_students(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.Students).offset(skip).limit(limit).all()


def create_student(db: Session, data: schema.StudentBase):
    db_user = model.Students(student_surname=data.student_surname, student_name=data.student_name,
                             student_class=data.student_class, student_uid=uuid.uuid4())
    try:
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
    except Exception as e:
        print(e)
    return db_user


def get_borrowers(db: Session, skip: int = 0, limit: int = 100):
    db_users = db.query(
        model.Books.book_name, model.Books.book_author_surname, model.Books.book_author,
        model.Books.library_id, model.Books.school, model.Books.date_of_issue,
        model.Students.student_surname, model.Students.student_name,
        model.Students.student_class).filter(model.Books.student_uid.notin_([uuid.UUID(int=0)]))
    return db_users.join(model.Students).offset(skip).limit(limit).all()
