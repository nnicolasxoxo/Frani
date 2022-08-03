from datetime import datetime
from tokenize import String
from mysqlx import Column, Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import column, Integer, string, DateTime

engine = create_engine('postgresql://')
Base= declarative_base()

class user(Base):
    __tablename__= 'users'

    id= column (Integer(), primary_key=True)
    username= Column(String(50),nullable=False, unique=True)
    email= Column (String(50), nullable=False, unique=True)
    created_at = Column(DateTime(), default=datetime.now())

    def __str__(self):
        return self.username

Session= sessionmaker (engine)
session= Session()

if __name__== '__main__':
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
