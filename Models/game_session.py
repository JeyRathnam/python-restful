from Main import db
from serializer.JsonSerializer import JsonSerializer

class Game_session(db.Model, JsonSerializer):
    __tablename__ = 'game_session'
    session_id = db.Column(db.Integer,primary_key=True, autoincrement=True)
    ip_address = db.Column(db.String)
    game_id = db.Column(db.Integer,db.ForeignKey('games.game_id'))
    player_count = db.Column(db.Integer)
    winning_user = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    session_start_time = db.Column(db.String)


    def __init__(self,_ip_address, _game_id, _player_count , _winning_user,_session_start_time):
        self.ip_address = _ip_address
        self.game_id = _game_id
        self.player_count = _player_count
        self.winning_user = _winning_user
        self.session_start_time = _session_start_time