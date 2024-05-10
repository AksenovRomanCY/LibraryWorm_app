from sqlalchemy.orm import Session

import models as model
from schemas import schema_student as schema


def get_student_by_id(db: Session, student_uid: str):
    return db.query(model.Students).filter(model.Students.student_uid == student_uid).first()


def get_student_by_name(db: Session, student_name: str):
    return db.query(model.Students).filter(model.Students.student_name == student_name).first()


def get_students(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.Students).offset(skip).limit(limit).all()


def create_student(db: Session, data: schema.StudentBase):
    db_user = model.Students(student_name=data.student_name, student_class=data.student_class)
    try:
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
    except Exception as e:
        print(e)
    return db_user


def update_student_by_id(db: Session, student_uid: str, data: schema.StudentBase):
    db_user = db.query(model.Students).filter(model.Students.student_uid == student_uid).first()
    db_user.student_name = data.student_name
    db_user.student_class = data.student_class
    try:
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
    except Exception as e:
        print(e)
    return db_user
