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
