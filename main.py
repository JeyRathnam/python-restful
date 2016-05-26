from flask import Flask
from flask_restful import Api
from flask.ext.httpauth import HTTPBasicAuth
import config
import model

auth = HTTPBasicAuth()

auth = HTTPBasicAuth()
app = Flask(__name__)
api = Api(app)


from account import account

#resource URI's

api.add_resource(account.createAccount, '/createAccount')
api.add_resource(account.Login, '/Login')


api.add_resource(account.getUsername, '/getUsername')



if __name__ == '__main__':
    app.run(debug=True)
