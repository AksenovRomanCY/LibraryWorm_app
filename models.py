import uuid
from sqlalchemy import Boolean, String, Column, Uuid, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class Students(Base):
    __tablename__ = "students"

    student_uid = Column(Uuid, primary_key=True, unique=True)

    student_surname = Column(String, index=True)
    student_name = Column(String, index=True)
    student_class = Column(String, index=True, default=None)


class Books(Base):
    __tablename__ = "books"

    book_uid = Column(Uuid, primary_key=True, unique=True)

    library_id = Column(String, index=True)
    book_name = Column(String, index=True)
    book_author_surname = Column(String, index=True)
    book_author = Column(String, index=True)
    book_description = Column(String, index=True, default=None)
    school = Column(String, index=True)
    language = Column(String, index=True)

    available = Column(Boolean, default=True)
    date_of_issue = Column(String, index=True, default='0000-00-00')

    student_uid = Column(Uuid, ForeignKey("students.student_uid"),
                         primary_key=False, unique=False, default=uuid.UUID(int=0))

    student = relationship("Students", primaryjoin="Books.student_uid==Students.student_uid")
