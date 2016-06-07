from Main import db
from flask_restful import Resource
from flask import request
from flask_sqlalchemy import SQLAlchemy
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

    def verify_password(self, password):
        return pwd_context.verify(password, self.password)

    def hash_password(self, password):
        self.password = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password)

class Login(Resource):
    def post(self):
        try:
            value = request.get_json(silent=True)
            username = value['username']
            password = value['password']
            device_name = value['device_name']
            user = User.query.filter_by(username=username).first()
            if user and user.verify_password(password):
                session = Session.SessionClass(user_id = user.user_id, creation_date = datetime.datetime.now(),ip_address = request.remote_addr,device_name = device_name , is_remember_me = 2)
                session.session_id = session.generate_session()
                session.__attributes__ = ['user_id', 'session_id', 'is_remember_me']
                db.session.add(session)
                dict = session.serialize()
                db.session.commit()
                return dict, 200
        except Exception as e:
            db.session.rollback()
            db.session.flush()
            return {'error' : str(e)}



class createAccount(Resource):
    def post(self):
        first_name = request.json.get('firstname')
        last_name = request.json.get('lastname')
        last_name = request.json.get('lastname')
        username = request.json.get('username')
        password = request.json.get('password')
        date_of_birth = request.json.get('dob')
        phone_number = request.json.get('phonenumber')
        if username is None or password is None:
            return {'error' : 1, 'error-message' : 'missing input arguments'}    # missing arguments
        if User.query.filter_by(username=username).first() is not None:
            return {'error': 1, 'error-message' : "username taken"}    # existing user
        user = User(username=username , first_name = first_name,last_name = last_name,phone_number = phone_number,date_of_birth = date_of_birth)
        user.hash_password(password)
        #db.session.expire_on_commit = False
        db.session.add(user)
        db.session.commit()
        return {'username': user.username}, 201

