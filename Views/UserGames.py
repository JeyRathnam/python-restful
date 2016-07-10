from flask_restful import Resource
from flask import request
from Models import Games,UserGames
from Main import db
import Decorators,datetime

class getUserGames(Resource):
    @Decorators.login_required
    def post(self):
        return True

class setUserGame(Resource):
    @Decorators.login_required
    def post(self,**kwargs):
        try:
            data = request.get_json(silent=True)
            user_id = kwargs['user_id']
            game_id = data['game_id']
            last_played = datetime.datetime.now()
            UserGame = UserGames.UserGames(user_id, game_id, last_played)
            db.session.add(UserGame)
            db.session.commit()
            return {'error' : 0}
        except Exception as e:
            return  {'error' : e}