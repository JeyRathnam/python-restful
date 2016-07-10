from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from Config import config

app = Flask(__name__)

app.config['SECRET_KEY'] = config['SECRET_KEY']
app.config['SQLALCHEMY_DATABASE_URI'] = config['sqlAlchemy']['SQLALCHEMY_DATABASE_URI']
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = config['sqlAlchemy']['SQLALCHEMY_COMMIT_ON_TEARDOWN']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config['sqlAlchemy']['SQLALCHEMY_TRACK_MODIFICATIONS']


api = Api(app)
db = SQLAlchemy(app)


from Views import Account,Test,UserGames

api.add_resource(Account.Login, '/Login')
api.add_resource(Account.createAccount, '/createAccount')
api.add_resource(UserGames.setUserGame, '/setUserGame')
api.add_resource(Test.Test,'/Test')

if config['SERVER_ENVIRONMENT'] == 'DEBUG':
    if __name__ == '__main__':
        app.run(debug=True)
elif config['SERVER_ENVIRONMENT'] == 'PROD':
    if __name__ == '__main__':
        app.run(host = '0.0.0.0')