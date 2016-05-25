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

	def __repr__(self):
	       return "<User(fname='%s', lname='%s', password='%s')>" % (self.first_name, self.last_name, self.password)

Base.prepare(dbconnect.engine)
