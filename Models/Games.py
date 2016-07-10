from Main import db
from serializer.JsonSerializer import JsonSerializer

class Games(db.Model, JsonSerializer):
    __tablename__ = 'games'
    game_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    game_title = db.Column(db.String)
    game_desc = db.Column(db.String)

