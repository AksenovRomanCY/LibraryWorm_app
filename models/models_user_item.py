from sqlalchemy import Boolean, String, Integer, ForeignKey, Column
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = "users"
    # The __tablename__ attribute tells SQLAlchemy the name of the table

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")


class Item(Base):
    __tablename__ = "items"
    # The __tablename__ attribute tells SQLAlchemy the name of the table

    id = Column(Integer, primary_key=True)
    tittle = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")
