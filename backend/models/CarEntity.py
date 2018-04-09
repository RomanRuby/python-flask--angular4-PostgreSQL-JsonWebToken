from marshmallow import Schema, fields
from sqlalchemy import Column, String

from .Entity import Entity, Base


class CarEntity(Entity, Base):
    __tablename__ = 'cars'

    name = Column(String)
    weight = Column(String)

    def __init__(self, name, weight):
        Entity.__init__(self)
        self.name = name
        self.weight = weight


class CarEntitySchema(Schema):
    id = fields.Number()
    name = fields.Str()
    weight = fields.Str()
