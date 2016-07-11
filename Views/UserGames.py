from flask_restful import Resource
from flask import request
from Models import Games,UserGames
from Main import db
import Decorators,datetime,json

class getUserGames(Resource):
    @Decorators.login_required
    def post(self,**kwargs):
        try:
            _user_id = kwargs['user_id']
            usergames =  UserGames.UserGames.query.filter_by(user_id = _user_id).all()
            gameList = []
            for usergame in usergames:
                gameDesc = Games.Games.query.filter_by(game_id = usergame.game_id).first()
                gameList.append(gameDesc.game_title)
            return {'games': gameList}
        except Exception as e:
            return e

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