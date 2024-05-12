import uuid
from sqlalchemy import Boolean, String, Column, Uuid, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class Students(Base):
    __tablename__ = "students"

    student_uid = Column(Uuid, primary_key=True, unique=True)

    student_name = Column(String, index=True)
    student_class = Column(String, index=True, default=None)


class Books(Base):
    __tablename__ = "books"

    book_uid = Column(Uuid, primary_key=True, unique=True)

    library_id = Column(String, index=True)
    book_name = Column(String, index=True)
    book_author = Column(String, index=True, default=None)
    book_description = Column(String, index=True, default=None)

    available = Column(Boolean, default=True)
    student_uid = Column(Uuid, ForeignKey("students.student_uid"),
                         primary_key=False, unique=False, default=uuid.UUID(int=0))

    student = relationship("Students", primaryjoin="Books.student_uid==Students.student_uid")
