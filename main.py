from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
import config

app = Flask(__name__)
api = Api(app)

test = '123'

def db_connect():
    print('before connect')
    engine = create_engine(config.SQLALCHEMY_DATABASE_URI)
    print('after connect')
    db = engine.connect()
    return db

# app.config.from_object('config')
# db = SQLAlchemy(app)
# print(db)


from first_package import first
from second_package import second

#resource URI's
api.add_resource(first.First,'/')
api.add_resource(second.SecondPackage, '/seperatesecond')

if __name__ == '__main__':
    app.run(debug=True)
