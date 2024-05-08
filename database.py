from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# Opening(or create) a file with the SQLite database

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
# Create a SQLAlchemy "engine"

SessionLocal = sessionmaker(autoflush=False, bind=engine)
# Each instance of the SessionLocal class will be a database session

Base = declarative_base()
# Later we will inherit from this class to create each of the database models or classes(the ORM models)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
    '''
    We need to have an independent database session/connection (SessionLocal) per request, 
    use the same session through all the request and then close it after the request is finished.
    '''