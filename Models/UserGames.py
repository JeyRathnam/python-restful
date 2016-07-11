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
    game_kills = db.Column(db.Integer)
    game_deaths = db.Column(db.Integer)
    game_wins = db.Column(db.Integer)
    game_seconds = db.Column(db.Integer)

    __attributes__ = ['user_id', 'game_id', 'last_played', 'game_kills' , 'game_deaths' , 'game_wins' , 'game_seconds']

    __required__ = ['user_id', 'game_id', 'last_played', 'game_kills' , 'game_deaths' , 'game_wins' , 'game_seconds']

    __attribute_serializer__ = dict(user_id='user_id', game_id='game_id', last_played='last_played',game_kills='game_kills' , game_deaths = 'game_deaths' , game_wins = 'game_wins',game_seconds = 'game_seconds')

    serializers = dict(
        user_id=dict(
            serialize=lambda x: str(x),
            deserialiez=lambda x: str(x)
        ),
        game_id=dict(
            serialize=lambda x: str(x),
            deserialize=lambda x: str(x)
        ),
        last_played=dict(
            serialize=lambda x: str(x),
            deserialize=lambda x: str(x)
        ),
        game_kills=dict(
            serialize=lambda x: str(x),
            deserialize=lambda x: str(x)
        ),
        game_deaths=dict(
            serialize=lambda x: str(x),
            deserialize=lambda x: str(x)
        ),
        game_wins=dict(
            serialize=lambda x: str(x),
            deserialize=lambda x: str(x)
        ),
        game_seconds=dict(
            serialize=lambda x: str(x),
            deserialize=lambda x: str(x)
        )
    )

    def __init__(self, _user_id, _game_id, _last_played):
        self.user_id = _user_id
        self.game_id = _game_id
        self.last_played = _last_played
        self.game_kills = 0
        self.game_deaths = 0
        self.game_wins = 0
        self.game_seconds = 0

