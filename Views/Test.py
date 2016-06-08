from flask_restful import Resource
from flask import request
import Decorators


class Test(Resource):
    @Decorators.login_required
    def post(self):
        return {'session test' : request.headers.get('virtu-auth')}

