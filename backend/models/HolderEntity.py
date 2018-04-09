from marshmallow import Schema, fields
from sqlalchemy import Column, String, Integer, ForeignKey

from .Entity import Entity, Base


class HolderEntity(Entity, Base):
    __tablename__ = 'holders'

    name = Column(String)
    key = Column(String)
    carsId = Column(Integer, ForeignKey('cars.id'))

    def __init__(self, name, key, carsId):
        Entity.__init__(self)
        self.name = name
        self.key = key
        self.carsId = carsId


class HolderEntitySchema(Schema):
    id = fields.Number()
    name = fields.Str()
    key = fields.Str()
    carsId = fields.Number()
