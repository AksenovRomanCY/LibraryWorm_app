from typing import Union
from pydantic import BaseModel


class StudentBase(BaseModel):
    student_surname: str
    student_name: str
    student_class: Union[str, None] = None


class StudentSee(StudentBase):
    book_name: str
    book_author_surname: str
    book_author: str
    school: str
    date_of_issue: str
    library_id: str
