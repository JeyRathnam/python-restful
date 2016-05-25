from first_package import first
from flask_restful import Resource
from datetime import datetime,date
from database import dbconnect

class SecondPackage(Resource):
    def get(self):
        session = dbconnect.Session()
        date_str = '30-01-12'
        formatter_string = "%d-%m-%y"
        datetime_object = datetime.strptime(date_str, formatter_string)

        ed_user = dbconnect.User(first_name='Ed Jones',last_name = 'last name',username = 'userwename', password='edspassword',date_of_birth = datetime_object.date(), phone_number = 123)
        session.add(ed_user)
        session.commit()
        session.close()
        return {'hello' : 'world'}
    def post(self):
        return {'first' : 'post'}
