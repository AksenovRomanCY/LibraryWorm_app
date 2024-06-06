from sqlalchemy.orm import Session
import uuid

import models as model
from schemas import schema_student as schema


def get_students(db: Session):
    return db.query(model.Students).all()


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


def get_student(db: Session, student_surname: str, student_name: str):
    return db.query(model.Students).filter(model.Students.student_name == student_name,
                                           model.Students.student_surname == student_surname).first()


def remove_book(db: Session, data: schema.StudentBase):
    db_user = db.query(model.Books).filter(
                                            model.Books.student_surname == data.student_surname,
                                            model.Students.student_name == data.student_name,
                                            model.Students.st_class == data.student_class).first()
    try:
        db.delete(db_user)
        db.commit()
        db.refresh(db_user)
    except Exception as e:
        print(e)
    return db_user
