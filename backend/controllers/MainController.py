from flask_jwt import jwt_required
from flask_restful import Resource


class MainController(Resource):
    decorators = [jwt_required()]

    def get(self):
        return "Main"
