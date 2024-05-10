from pydantic import BaseModel


class UserBase(BaseModel):
    name: str
    is_active: bool


class User(UserBase):
    id: int
