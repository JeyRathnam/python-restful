from sqlalchemy.ext.declarative import declarative_base, DeferredReflection
from sqlalchemy import Column, Integer, String
from database import dbconnect
from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)
import config


Base = declarative_base(cls=DeferredReflection)


class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    username = Column(String)
    password = Column(String)
    date_of_birth = Column(String)
    phone_number = Column(Integer)

    def generate_auth_token(self, expiration = 600):
        s = Serializer(config.APP_KEY, expires_in = expiration)
        return s.dumps({ 'id': self.id })

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(config.SECRET_KEY)
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None  # valid token, but expired
        except BadSignature:
            return None  # invalid token
        user = User.query.get(data['id'])
        return user


Base.prepare(dbconnect.engine)
