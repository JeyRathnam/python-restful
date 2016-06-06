from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import main

db = SQLAlchemy(main.app)
#engine = create_engine(config.SQLALCHEMY_DATABASE_URI, echo=False)
#Session = sessionmaker(bind=engine)
