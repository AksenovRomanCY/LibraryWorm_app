from sqlalchemy import Boolean, String, Integer, Column

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, unique=True, index=True)
    name = Column(String, index=True)
    is_active = Column(Boolean, default=True)
