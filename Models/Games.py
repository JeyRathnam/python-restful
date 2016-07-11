from Main import db
from serializer.JsonSerializer import JsonSerializer

class Games(db.Model, JsonSerializer):
    __tablename__ = 'games'
    game_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    game_title = db.Column(db.String)
    game_desc = db.Column(db.String)

    __attributes__ = ['game_id', 'game_title' , 'game_desc']

    __required__ = ['game_id', 'game_title' , 'game_desc']

    __attribute_serializer__ = dict(game_id='game_id', game_title='game_title', game_desc='game_desc')

    serializers = dict(
        game_id=dict(
            serialize=lambda x: str(x),
            deserialiez=lambda x: str(x)
        ),
        game_title=dict(
            serialize=lambda x: str(x),
            deserialize=lambda x: str(x)
        ),
        game_desc=dict(
            serialize=lambda x: str(x),
            deserialize=lambda x: str(x)
        )
    )