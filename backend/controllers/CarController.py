from flask import jsonify
from flask_jwt import jwt_required
from flask_restful import Resource

from backend.services.CarService import CarService

carService = CarService()


class CarController(Resource):
    decorators = [ jwt_required()]

    def get(self):
        cars = carService.getCars()
        return jsonify(cars.data)

    def delete(self, carId):
        carService.deleteCar(carId=carId)
        return '', 201
