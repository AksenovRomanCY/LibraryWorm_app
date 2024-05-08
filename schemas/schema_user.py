from pydantic import BaseModel


class UserBase(BaseModel):
    name: str

    # Common attribute while creating or reading data


'''
class UserCreate(UserBase):
    id: int
    # Additional data (attributes) needed for creation
'''


class User(UserBase):
    is_active: bool
    id: int


