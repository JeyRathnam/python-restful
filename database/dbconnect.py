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

Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)

# session = Session()
#
#
# date_str = '30-01-12'
# formatter_string = "%d-%m-%y"
# datetime_object = datetime.strptime(date_str, formatter_string)
#
#
# ed_user = User(user_id=1, first_name='Ed Jones',last_name = 'last name',username = 'username', password='edspassword',date_of_birth = datetime_object.date(), phone_number = 123)
# session.add(ed_user)
# session.commit()
