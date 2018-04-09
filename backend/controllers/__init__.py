from flask import Flask
from flask_jwt import JWT, current_identity, jwt_required
from flask_restful import Resource, Api, abort
from backend.configs.Authorities import authenticate, identity
from backend.controllers.CarController import CarController
from backend.controllers.HolderController import HolderController
from backend.controllers.LoginController import Login
from backend.controllers.MainController import MainController
from backend.models.Entity import engine, Base


app = Flask(__name__)
api = Api(app)
app.config['SECRET_KEY'] = 'super-secret'
jwt = JWT(app, authenticate, identity)

api.add_resource(MainController, '/')
api.add_resource(Login, '/account')
api.add_resource(HolderController, '/holders')
api.add_resource(CarController, '/cars', '/cars/<carId>')
