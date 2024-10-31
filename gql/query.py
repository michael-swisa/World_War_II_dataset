import graphene
import sqlalchemy.orm.query

from db.database import db_session
from gql.types import MissionType, CityType, TargetType, CountryType
from models.city import CityModel
from models.country import CountryModel
from models.mission import MissionModel
from models.target import TargetModel


class Query(graphene.ObjectType):
    mission_by_id = graphene.Field(MissionType, mission_id=graphene.Int(required=True))
    missions_in_the_date_range = graphene.List(MissionType, start_date=graphene.Date(required=True),
                                               end_date=graphene.Date(required=True))

    missions_by_country = graphene.List(MissionType, country_name=graphene.String(required=True))
    missions_by_target_industry = graphene.List(MissionType, target_industry=graphene.String(required=True))

    @staticmethod
    def resolve_mission_by_id(root, info, mission_id):
        query_model = db_session.query(MissionModel).filter(
            MissionModel.mission_id == mission_id).first()

        return query_model

        # query_model: sqlalchemy.orm.query.Query = db_session.query(MissionModel)
        # return query_model.join(MissionModel.targets).first()

    @staticmethod
    def resolve_missions_in_the_date_range(root, info, start_date, end_date):
        return db_session.query(MissionModel).filter(MissionModel.mission_date.between(start_date, end_date)).all()

    @staticmethod
    def resolve_missions_by_country(root, info, country_name):
        country = db_session.query(CountryModel).filter(CountryModel.country_name == country_name).first()

        missions = (db_session.query(MissionModel)
                    .join(MissionModel.targets)
                    .join(TargetModel.city)
                    .filter(CityModel.country_id == country.country_id)
                    .all())

        return missions

    @staticmethod
    def resolve_missions_by_target_industry(root, info, target_industry):
        return (db_session.
                query(MissionModel)
                .join(MissionModel.targets)
                .filter(TargetModel.target_industry == target_industry)
                .all())



