from typing import Union
from pydantic import BaseModel


class BookBase(BaseModel):
    book_name: str
    book_author_surname: str
    book_author: str
    book_description: Union[str, None] = None
    school: str


class BookCreate(BookBase):
    library_id: str
    language: str


class BookSee(BookCreate):
    available: bool
    date_of_issue: str
    student_name: str
    student_class: str
