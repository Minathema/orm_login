import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tabledef import *

engine = create_engine('sqlite:///credentials.db', echo=True) #connect to database

Session = sessionmaker(bind=engine)
session = Session()

#add new user data to "users" table in database
user = User("admin1", "password1")
session.add(user)

user = User("admin2", "password2")
session.add(user)

user = User("admin3", "password3")
session.add(user)

session.commit()

session.commit()
