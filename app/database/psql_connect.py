import os
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from app.models import Base

load_dotenv(verbose=True)

SQL_URI = os.getenv('DATABASE_URL')

engine = create_engine(SQL_URI)
session_maker = sessionmaker(bind=engine)

def init_db():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    with session_maker() as session:
        session.commit()

if __name__ == '__main__':
    init_db()
