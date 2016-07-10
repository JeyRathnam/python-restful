from flask_restful import Resource
from Models import Games,UserGames
import Decorators

class getUserGames(Resource):
    @Decorators.login_required
    def post(self):
        return True

class setUserGame(Resource):
    @Decorators.login_required
    def post(self,**kwargs):
        print(kwargs['user'])