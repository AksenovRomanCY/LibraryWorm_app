from sqlalchemy import Boolean, String, Integer, Column, uuid

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, unique=True)
    name = Column(String, index=True)
    is_active = Column(Boolean, default=True)


class Students(Base):
    __tablename__ = "Student"

    student_uid = Column(uuid, primary_key=True, unique=True)

    student_name = Column(String, index=True)
    student_class = Column(String, index=True)


class Books(Base):
    __tablename__ = "Books"

    book_uid = Column(uuid, primary_key=True, unique=True)

    library_id = Column(String, index=True)
    book_name = Column(String, index=True)
    book_author = Column(String, index=True)
    book_description = Column(String, index=True)

    available = Column(Boolean, default=True)
    student_uid = Column(uuid, primary_key=True, unique=True, default=None)
