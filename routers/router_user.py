from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db

from crud import crud_user as crud
from schemas import schema_user as schema

router = APIRouter()


@router.post('/users/', response_model=schema.User)
def create_user(data: schema.User = None, db: Session = Depends(get_db)):  # UserCreate
    db_user = crud.get_user_by_name(db, name=data.name)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, data=data)


@router.get("/users/", response_model=list[schema.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@router.get("/users/{int(user_id)}", response_model=schema.User)
def read_user_by_id(user_id: int = None, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_id(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.get("/users/{str(name)}", response_model=schema.User)
def get_user_by_name(name: str = None, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_name(db, name=name)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.put("/users/{user_id}", response_model=schema.User)
def update_user_by_id(data: schema.User = None, user_id: int = None, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_id(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.update_user_by_id(data=data, db=db, user_id=user_id)
