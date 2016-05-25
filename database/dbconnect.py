from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
import config

engine = create_engine(config.SQLALCHEMY_DATABASE_URI, echo=True)
Base = declarative_base()

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

Session = sessionmaker(bind=engine)
