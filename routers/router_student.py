from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db

from crud import crud_student as crud
from schemas import schema_student as schema

router = APIRouter()


@router.post('/students/', response_model=schema.StudentBase)
def create_student(data: schema.StudentBase = None, db: Session = Depends(get_db)):  # UserCreate
    return crud.create_student(db=db, data=data)


@router.get("/students/", response_model=list[schema.StudentBase])
def get_students(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_students(db, skip=skip, limit=limit)


@router.get("/students/{str(student_uid)}", response_model=schema.StudentBase)
def get_student_by_uid(student_uid: str = None, db: Session = Depends(get_db)):
    db_user = crud.get_student_by_uid(db, student_uid=student_uid)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.get("/students/{str(student_name)}", response_model=schema.StudentBase)
def get_student_by_name(student_name: str = None, db: Session = Depends(get_db)):
    db_user = crud.get_student_by_name(db, student_name=student_name)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.put("/students/{str(student_uid)}", response_model=schema.StudentBase)
def update_student_by_uid(data: schema.StudentBase = None, student_uid: str = None, db: Session = Depends(get_db)):
    db_user = crud.get_student_by_uid(db, student_uid=student_uid)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.update_student_by_uid(data=data, db=db, student_uid=student_uid)
