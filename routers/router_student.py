from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db

from crud import crud_student as crud
from schemas import schema_student as schema

router = APIRouter()


@router.post('/create_student', response_model=schema.StudentBase)
def create_student(data: schema.StudentBase = None, db: Session = Depends(get_db)):
    return crud.create_student(db=db, data=data)


@router.get("/get_students_all", response_model=list[schema.StudentBase])
def get_students_all(db: Session = Depends(get_db)):
    return crud.get_students(db)


@router.get("/get_student/{str(student_surname)}/{str(student_name)}",
            response_model=schema.StudentBase)
def get_student(student_surname: str = None, student_name: str = None, db: Session = Depends(get_db)):
    db_user = crud.get_student(db, student_surname=student_surname, student_name=student_name)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.delete("/remove_student/{str(student_surname)}/{str(student_name)}/{str(student_class)}", response_model=schema.StudentBase)
def remove_student(student_surname: str = None, student_name: str = None,
                   student_class: str = None, db: Session = Depends(get_db)):
    db_user = crud.get_student(db, student_surname=student_surname, student_name=student_name)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.remove_book(db=db, student_surname=student_surname,
                            student_name=student_name, student_class=student_class)
