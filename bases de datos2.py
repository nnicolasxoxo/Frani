from datetime import datetime
from tokenize import String
from mysqlx import Column, Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, DateTime

engine = create_engine('mysql+pymysql://admin:123456PROG@localhost/peliculas')
Base= declarative_base()

class pelicula(Base):
    __tablename__= 'peliculas'

    id= Column (Integer(), primary_key=True)
    nombre = Column(String(50),nullable=False, unique=True)
    genero = Column (String(50), nullable=False, unique=True)
    descripcion = Column (String(100), nullable=False, unique=True)
    duración = Column (String(50), nullable=False, unique=True)
    created_at = Column(DateTime(), default=datetime.now())

    def __str__(self):
        return self.nombre

Session= sessionmaker (engine)
session= Session()

if __name__== '__main__':
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)