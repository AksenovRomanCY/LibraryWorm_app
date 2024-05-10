from typing import Union
from pydantic import BaseModel


class StudentBase(BaseModel):
    student_name: str
    student_class: Union[str, None] = None
