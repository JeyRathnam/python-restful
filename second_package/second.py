from first_package import first
from flask_restful import Resource
import main

class SecondPackage(Resource):
    def get(self):

        try:
            con = main.db_connect()
            res = con.execute('insert into users(first_name,last_name,username,password,date_of_Birth,phone_Number) values(\'jey\',\'rathnam\',\'jairathnem1\',\'password\',\'1990-12-10\',100);')
        except Exception:
            return {'error' : 'dberror'},500
        finally:
            con.close()
        return {'hello' : 'world'}
    def post(self):
        return {'first' : 'post'}
