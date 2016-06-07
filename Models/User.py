from Main import db
from passlib.apps import custom_app_context as pwd_context
from Models import Session
import datetime
import sqlalchemy,builtins,json
from serializer.JsonSerializer import JsonSerializer

class User(db.Model, JsonSerializer):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    username = db.Column(db.String)
    password = db.Column(db.String)
    date_of_birth = db.Column(db.String)
    phone_number = db.Column(db.Integer)

    def __init__(self, _first_name, _last_name, _username, _password, _date_of_birth, _phone_number):
        self.first_name = _first_name
        self.last_name = _last_name
        self.username = _username
        self.password = _password
        self.date_of_birth = _date_of_birth
        self.phone_number = _phone_number


    def verify_password(self, password):
        return pwd_context.verify(password, self.password)

    def hash_password(self, password):
        self.password = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password)



