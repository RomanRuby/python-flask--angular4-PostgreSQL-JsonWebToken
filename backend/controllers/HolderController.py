from flask import jsonify
from flask_jwt import jwt_required
from flask_restful import Resource

from backend.services.HolderService import HolderService


holderService = HolderService()


class HolderController(Resource):
    decorators = [ jwt_required()]

    def get(self):
        cars = holderService.getHolders()
        return jsonify(cars.data)
