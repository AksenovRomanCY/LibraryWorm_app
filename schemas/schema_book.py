from typing import Union
from pydantic import BaseModel


class BookBase(BaseModel):
    book_name: str
    book_author: Union[str, None] = None
    book_description: Union[str, None] = None
    school: str


class BookCreate(BookBase):
    library_id: str
    language: str


class BookSee(BookCreate):
    available: bool
    student_name: str
    student_class: str

