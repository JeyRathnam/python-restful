from flask_restful import Resource

class First(Resource):
    def get(self):
        return {'hello' : 'world'}
    def post(self):
        return {'first' : 'post'}
