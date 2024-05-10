from sqlalchemy.orm import Session

import models as model
from schemas import schema_user as schema


# In this file we will have reusable functions to interact with the data in the database.


def get_user_by_id(db: Session, user_id: int):
    return db.query(model.User).filter(model.User.id == user_id).first()


def get_user_by_name(db: Session, name: str):
    return db.query(model.User).filter(model.User.name == name).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.User).offset(skip).limit(limit).all()


def create_user(db: Session, data: schema.User):  # UserCreate
    db_user = model.User(name=data.name, id=data.id)
    try:
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
    except Exception as e:
        print(e)
    return db_user


def update_user_by_id(db: Session, user_id: int, data: schema.UserBase):
    db_user = db.query(model.User).filter(model.User.id == user_id).first()
    db_user.name = data.name
    db_user.is_active = data.is_active
    try:
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
    except Exception as e:
        print(e)
    return db_user




