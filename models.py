from sqlalchemy import Boolean, String, Column, Uuid

from database import Base


class Students(Base):
    __tablename__ = "students"

    student_uid = Column(Uuid, primary_key=True, unique=True)

    student_name = Column(String, index=True)
    student_class = Column(String, index=True)


class Books(Base):
    __tablename__ = "books"

    book_uid = Column(Uuid, primary_key=True, unique=True)

    library_id = Column(String, index=True)
    book_name = Column(String, index=True)
    book_author = Column(String, index=True)
    book_description = Column(String, index=True)

    available = Column(Boolean, default=True)
    student_uid = Column(Uuid, primary_key=True, unique=True, default=None)
