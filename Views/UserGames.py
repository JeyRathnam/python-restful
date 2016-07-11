from flask_restful import Resource
from flask import request
from Models import Games,UserGames
from Main import db
import Decorators,datetime

class getUserGames(Resource):
    @Decorators.login_required
    def post(self,**kwargs):
        try:
            _user_id = kwargs['user_id']
            usergames =  UserGames.UserGames.query.filter_by(user_id = _user_id).all()
            gameList = []
            for usergame in usergames:
                game = Games.Games.query.filter_by(game_id = usergame.game_id).first()
                usergame.__attributes__ = ['last_played', 'game_kills' , 'game_deaths' , 'game_wins' , 'game_seconds']
                game.__attributes__ = ['game_title' , 'game_desc']
                usergameSerialize = usergame.serialize()
                gameserialize = game.serialize()
                usergameSerialize['game_title'] = gameserialize['game_title']
                usergameSerialize['game_desc'] = gameserialize['game_desc']
                gameList.append(usergameSerialize)
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