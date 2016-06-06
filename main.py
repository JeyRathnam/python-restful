from flask import Flask
from flask_restful import Api
from flask.ext.httpauth import HTTPBasicAuth
import config

auth = HTTPBasicAuth()
app = Flask(__name__)

app.config['SECRET_KEY'] = config.APP_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
api = Api(app)


from account import account

#resource URI's

api.add_resource(account.createAccount, '/createAccount')
api.add_resource(account.Login, '/Login')


api.add_resource(account.getUsername, '/getUsername')



if __name__ == '__main__':
    app.run(debug=True)
