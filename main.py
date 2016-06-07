from flask import Flask, abort, request, jsonify, g, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask_restful import Api
from Config import config

app = Flask(__name__)

app.config['SECRET_KEY'] = config['SECRET_KEY']
app.config['SQLALCHEMY_DATABASE_URI'] = config['sqlAlchemy']['SQLALCHEMY_DATABASE_URI']
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = config['sqlAlchemy']['SQLALCHEMY_COMMIT_ON_TEARDOWN']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config['sqlAlchemy']['SQLALCHEMY_TRACK_MODIFICATIONS']


api = Api(app)

db = SQLAlchemy(app)

from Views import Account

api.add_resource(Account.Login, '/Login')
api.add_resource(Account.createAccount, '/createAccount')

if __name__ == '__main__':
    app.run(debug=True)