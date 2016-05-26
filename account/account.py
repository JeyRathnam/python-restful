from flask_restful import Resource
from flask import Flask,g
from datetime import datetime,date
from database import dbconnect
from flask_restful import reqparse
from flask import jsonify,g
from passlib.apps import custom_app_context as pwd_context
from flask.ext.login import login_user , logout_user , current_user , login_required
import sqlalchemy.exc
from model import Models
import main



class createAccount(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('first_name', required=True, help='First name required')
        parser.add_argument('last_name', required=True, help='Last name required')
        parser.add_argument('username', required=True, help='user name required')
        parser.add_argument('password', required=True, help='pass required')
        parser.add_argument('date_of_birth', required=True, help='dob required')
        parser.add_argument('phone_number', required=True, help='phone number required')
        args = parser.parse_args()

        hashed_password = pwd_context.encrypt(args['password'])

        formatter_string = "%d-%m-%y"
        datetime_object = datetime.strptime(args['date_of_birth'], formatter_string)
        try:
            ed_user = Models.User(first_name=args['first_name'],last_name = args['last_name'],username =args['username'], password=hashed_password,date_of_birth = datetime_object.date(), phone_number = args['phone_number'])
            session = dbconnect.Session()
            session.add(ed_user)
            session.commit()
        except sqlalchemy.exc.IntegrityError as exc:
            return {'error' : 1,
                    'error-message' : 'User name already taken.'}
        session.close()
        return {'username' : args['username'],
                'error' : '0'}

class Login(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', required=True, help='user name required')
        parser.add_argument('password', required=True, help='pass required')
        args = parser.parse_args()
        session = dbconnect.Session()
        for user_details in session.query(Models.User.username,Models.User.password).filter(Models.User.username == args['username']):
            if(pwd_context.verify(args['password'],user_details[1])):
                return {'error' : 0, 'login' : 'success'}
            else:
                return {'error' : 1, 'login' : 'failed'}


@main.auth.verify_password
def verify_password(username, password):
    session = dbconnect.Session()
    for user_details in session.query(Models.User.username, Models.User.password).filter(
                    Models.User.username == username):
        if (pwd_context.verify(password, user_details[1])):
            g.User = user_details
            return True
        else:
            return False

class getUsername(Resource):
    @main.auth.login_required
    def get(self):
        token = Models.User.generate_auth_token()
        return jsonify({'token': token.decode('ascii')})
