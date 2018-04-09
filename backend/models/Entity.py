from datetime import datetime
from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from backend.configs import Credentials


db_url, db_name,db_user, db_password = Credentials.getCredentials()
engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_url}/{db_name}')
Session = sessionmaker(bind=engine)
Base = declarative_base()


class Entity:
    id = Column(Integer, primary_key=True)

    def __init__(self):
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
