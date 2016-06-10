from flask_restful import Resource
from Models import User,Session
from flask import request
from Main import db
import datetime

class Login(Resource):
    def post(self):
        try:
            value = request.get_json(silent=True)
            username = value['username']
            password = value['password']
            device_name = value['device_name']
            user = User.User.query.filter_by(username=username).first()
            if user and user.verify_password(password):
                session = Session.SessionClass(user.user_id, datetime.datetime.now(), None, request.environ['REMOTE_ADDR'], device_name, _is_remember_me=0)
                session.expiration_date = session.creation_date + datetime.timedelta(minutes=1440)
                session.session_id = session.generate_session()
                session.__attributes__ = [ 'session_id']
                db.session.add(session)
                dict = session.serialize()
                dict['username'] = user.username
                db.session.commit()
                return dict, 200
        except Exception as e:
            db.session.rollback()
            db.session.flush()



class createAccount(Resource):
    def post(self):
        values = request.get_json(silent=True)
        first_name = values['firstname']
        last_name = values['lastname']
        last_name = values['lastname']
        username = values['username']
        password = values['password']
        date_of_birth = values['dob']
        phone_number = values['phonenumber']
        if username is None or password is None:
            return {'error' : 1, 'error-message' : 'missing input arguments'}    # missing arguments
        if User.User.query.filter_by(username=username).first() is not None:
            return {'error': "username taken"}    # existing user
        user = User.User(first_name,last_name,username,password,date_of_birth,phone_number)
        user.hash_password(password)
        #db.session.expire_on_commit = False
        db.session.add(user)
        db.session.commit()
        return {'username': user.username}, 201