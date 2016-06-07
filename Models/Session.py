from Main import db
from flask import jsonify
import os, base64, random,string,json
from serializer.JsonSerializer import JsonSerializer
from Exceptions.InputValidationException import InputValidationException

class SessionClass(db.Model, JsonSerializer):
    __tablename__ = 'session'
    user_id = db.Column(db.Integer)
    session_id = db.Column(db.String, primary_key=True)
    creation_date = db.Column(db.String)
    expiration_date = db.Column(db.String)
    ip_address = db.Column(db.String)
    device_name = db.Column(db.String)
    is_remember_me = db.Column(db.BOOLEAN)

    __attributes__ = ['user_id' , 'session_id' ]

    __required__ = ['user_id', 'session_id']

    __attribute_serializer__ = dict(user_id='user_id', session_id='session_id' ,creation_date = 'creation_date', is_remember_me = 'is_remember_me' )

    serializers = dict(
        user_id=dict(
            serialize=lambda x: str(x),
            deserialiez=lambda x: str(x)
        ),
        session_id=dict(
            serialize=lambda x: str(x),
            deserialize = lambda x: str(x)
    ),
        creation_date = dict(
            serialize = lambda x: str(x),
            deserialize = lambda x: str(x)
    ),
        is_remember_me = dict(
            serialize = lambda  x: str(x),
            deserialize=lambda x: str(x)
        )
    )

    def generate_session(self):
        for x in range(10):
            session =  ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(30))
            sessionResult = SessionClass.query.filter_by(session_id = session).first()
            if sessionResult:
                continue
            else:
                return session

    def validate(self):
        for attr in self.__required__:
            val = getattr(self, attr)
            if not val:
                return InputValidationException("{} : input missing", attr)


    def jsonify(self):
        dict = {'user_id' : self.user_id , 'session_id' : self.session_id, "expiration_date" : self.expiration_date}
        return dict



    def to_JSON(self):
        return json.dumps(self, default=lambda o: _try(o),sort_keys=True, indent=4)
