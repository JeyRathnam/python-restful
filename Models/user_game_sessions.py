from Main import db
from serializer.JsonSerializer import JsonSerializer

class User_game_sessions(db.Model,JsonSerializer):
    __tablename__ = 'user_game_sessions'
    __table_args__ = (
        db.PrimaryKeyConstraint('user_id', 'session_id'),
    )
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    session_id = db.Column(db.Integer, db.ForeignKey('game_session.session_id'))
    join_time = db.Column(db.String)

    def __init__(self,_user_id, _session_id, _join_time):
        self.user_id = _user_id
        self.session_id = _session_id
        self.join_time = _join_time