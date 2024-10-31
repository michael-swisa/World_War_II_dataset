import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType

from models.city import CityModel
from models.country import CountryModel
from models.mission import MissionModel
from models.target import TargetModel
from models.targettype import TargetTypeModel


class CityType(SQLAlchemyObjectType):
    class Meta:
        model = CityModel
        interfaces = (graphene.relay.Node,)


class CountryType(SQLAlchemyObjectType):
    class Meta:
        model = CountryModel
        interfaces = (graphene.relay.Node,)


class MissionType(SQLAlchemyObjectType):
    class Meta:
        model = MissionModel
        interfaces = (graphene.relay.Node,)


class TargetType(SQLAlchemyObjectType):
    class Meta:
        model = TargetModel
        interfaces = (graphene.relay.Node,)


class TargettypeType(SQLAlchemyObjectType):
    class Meta:
        model = TargetTypeModel
        interfaces = (graphene.relay.Node,)
