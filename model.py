from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
import os
import hashlib

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    account = Column(String, unique=True)
    password_hash = Column(String)
    name = Column(String)

    def __init__(self, account, password, name):
        self.account = account
        self.password_hash = hashlib.md5(password.encode()).hexdigest()
        self.name = name

    @property
    def password(self):
        return self.password_hash

    @password.setter
    def password(self, password):
        self.password_hash = hashlib.md5(password.encode()).hexdigest()

    def verify_password(self,password):
        if hashlib.md5(password.encode()).hexdigest() == self.password:
            return True
        else:
            return False
    
    def __repr__(self):
        return '<User %r>' % self.name
    


engine = create_engine('sqlite:///memory.sqlite', echo=True)
Session = sessionmaker(bind=engine)
session = Session()
if not os.path.isfile('d:\\fff\\wrnmb\\memory.sqlite'):
    Base.metadata.create_all(engine)
    
    

'''    def __init__(self, account, password, name):
        self.account = account
        self.password = password
        self.name = name
'''
