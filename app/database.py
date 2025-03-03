from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError
from dotenv import load_dotenv
import os

load_dotenv()
db_pasword = os.getenv("DB_PASSWORD")

SQLALCHEMY_DATABASE_URL = f'postgresql+psycopg2://postgres:{db_pasword}@localhost/outer_rim_rally'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()