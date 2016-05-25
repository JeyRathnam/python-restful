from sqlalchemy.ext.declarative import declarative_base,DeferredReflection
from sqlalchemy import Column, Integer, String
from database import dbconnect


Base = declarative_base(cls = DeferredReflection)


class User(Base):
	__tablename__ = 'users'
	user_id = Column(Integer, primary_key=True)
	first_name = Column(String)
	last_name = Column(String)
	username = Column(String)
	password = Column(String)
	date_of_birth = Column(String)
	phone_number = Column(Integer)

Base.prepare(dbconnect.engine)
