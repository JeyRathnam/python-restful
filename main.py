from flask import Flask, abort, request, jsonify, g, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask_restful import Api
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy dog'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


api = Api(app)

db = SQLAlchemy(app)

from Models import User

api.add_resource(User.Login, '/Login')
api.add_resource(User.createAccount, '/createAccount')

if __name__ == '__main__':
    app.run(debug=True)