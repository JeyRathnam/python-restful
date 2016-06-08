from functools import wraps
from flask import request
from Models import Session

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