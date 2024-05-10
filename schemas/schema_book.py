from typing import Union
from pydantic import BaseModel


class BookBase(BaseModel):
    book_name: str
    book_author: Union[str, None] = None
    book_description: Union[str, None] = None


class BookCreate(BookBase):
    library_id: str
