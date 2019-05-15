from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite:///credentials.db', echo=True)
Base = declarative_base()


class User(Base):
    __tablename__ = "users" #declare table name
    id = Column(Integer, primary_key=True) #name of new column and input type
    username = Column(String) #name of new column and input type
    password = Column(String) #name of new column and input type


    def __init__(self, username, password):
        self.username = username
        self.password = password


Base.metadata.create_all(engine) #create table
