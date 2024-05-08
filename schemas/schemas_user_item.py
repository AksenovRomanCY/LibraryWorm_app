from pydantic import BaseModel


class ItemBase(BaseModel):
    title: str
    description: str | None = None
    # Common attribute while creating or reading data


class ItemCreate(ItemBase):
    pass
    # Additional data (attributes) needed for creation


class Item(ItemBase):
    id: int
    owner_id: int
    # Reading data, when returning it from the API.


class UserBase(BaseModel):
    email: str
    # Common attribute while creating or reading data


class UserCreate(UserBase):
    hashed_password: str
    # Additional data (attributes) needed for creation


class User(UserBase):
    id: int
    is_active: bool
    items: list[Item] = []
    # Reading data, when returning it from the API.
