from flask_restful import Resource
from functools import wraps
from Models import Session
from flask import request

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        virtuAuth = request.headers.get('virtu-auth')
        if virtuAuth is not None:
            session = Session.SessionClass.query.filter_by(session_id = virtuAuth).first()
            if session is None:
                return {'error' : 'login failed'}
        return f(*args, **kwargs)
    return decorated_function


class Test(Resource):
    @login_required
    def post(self):
        return {'session test' : request.headers.get('virtu-auth')}

