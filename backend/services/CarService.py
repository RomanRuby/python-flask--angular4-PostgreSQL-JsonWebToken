from backend.models.CarEntity import CarEntitySchema, CarEntity
from backend.models.Entity import Session


class CarService:

    def getCars(self):
        session = Session()
        exam_objects = session.query(CarEntity).all()

        schema = CarEntitySchema(many=True)
        cars = schema.dump(exam_objects)

        session.close()
        return cars

    def deleteCar(self, carId=None):
        session = Session()
        car = session.query(CarEntity).filter_by(id=carId).first()
        session.delete(car)
        session.commit()
        session.close()
