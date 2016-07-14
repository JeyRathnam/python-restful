from flask_restful import Resource
from Models import game_session,user_game_sessions,User
from flask import request
from Main import db
import datetime,Decorators,json


class CreateSession(Resource):
    server_session_start = None
    @Decorators.login_required
    def post(self,**kwargs):
        user_id = kwargs['user_id']
        available_session = None
        data = request.get_json(silent=True)
        game_id = data['game_id']
        all_current_sessions = game_session.Game_session.query.filter_by(game_id = game_id).all()
        if not all_current_sessions:
            available_session =  self.createSession(game_id)
        else:
            for individual_session in all_current_sessions:
                gotSession = False
                if(individual_session.player_count < 16):
                    available_session = individual_session
                    gotSession = True
            if not gotSession:
                self.createSession(game_id)

        check_user_session = user_game_sessions.User_game_sessions.query.filter_by(user_id = user_id, session_id = available_session.session_id).all()
        if not check_user_session:
            user_game_session = user_game_sessions.User_game_sessions(user_id,available_session.session_id,datetime.datetime.now())
            db.session.add(user_game_session)
            db.session.commit()

        print((str)(datetime.datetime.now()) + (str)(datetime.datetime.now().time()))
        all_users_in_session = user_game_sessions.User_game_sessions.query.filter_by(session_id = available_session.session_id).all()
        all_user_ids = []
        for value in all_users_in_session:
            all_user_ids.append(value.user_id)

        usernames = User.User.query.filter(User.User.user_id.in_(all_user_ids)).all()
        usernames_in_session = []
        for user in usernames:
            usernames_in_session.append(user.username)


        return {'users' : usernames_in_session, 'session start' : available_session.session_start_time}


    def createSession(self,game_id):
        new_game_session = game_session.Game_session('52.40.240.45', game_id, 1, None,((str)(datetime.datetime.now()) + (str)(datetime.datetime.now().time())) )
        db.session.add(new_game_session)
        db.session.commit()
        return  new_game_session