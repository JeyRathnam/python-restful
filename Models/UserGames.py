from Main import db
from serializer.JsonSerializer import JsonSerializer

class UserGames(db.Model, JsonSerializer):
    __tablename__ = 'user_games'
    __table_args__ = (
        db.PrimaryKeyConstraint('user_id', 'game_id'),
    )

    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    game_id = db.Column(db.Integer, db.ForeignKey('games.game_id'))
    last_played = db.Column(db.String)


    def __init__(self, _user_id, _game_id, _last_played):
        self.user_id = _user_id
        self.game_id = _game_id
        self.last_played = _last_played


