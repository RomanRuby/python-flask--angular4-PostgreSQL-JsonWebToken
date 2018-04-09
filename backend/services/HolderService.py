from backend.models.HolderEntity import HolderEntitySchema,HolderEntity
from backend.models.Entity import Session


class HolderService:

    def getHolders(self):
        session = Session()
        exam_objects = session.query(HolderEntity).all()

        schema = HolderEntitySchema(many=True)
        cars = schema.dump(exam_objects)

        session.close()
        return cars
