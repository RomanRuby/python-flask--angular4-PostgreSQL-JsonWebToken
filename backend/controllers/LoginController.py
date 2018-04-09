from flask_jwt import jwt_required, current_identity
from flask_restful import Resource


class Login(Resource):
    decorators = [jwt_required()]

    def get(self):
        return {'login': 'user1',
                'password': '1234'}
