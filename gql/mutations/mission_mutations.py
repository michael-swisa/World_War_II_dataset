from graphene import Field, Mutation
from sqlalchemy import Integer, Date, Numeric
from db.database import db_session
from gql.types import MissionType
from models.mission import MissionModel


class MissionInput(Mutation):
    class Arguments:
        mission_id = Integer()
        mission_date = Date()
        airborne_aircraft = Numeric()
        attacking_aircraft = Numeric()
        bombing_aircraft = Numeric()
        aircraft_returned = Numeric()
        aircraft_failed = Numeric()
        aircraft_damaged = Numeric()
        aircraft_lost = Numeric()

    mission = Field(MissionType)

    @staticmethod
    def mutate(root, info, mission_date, airborne_aircraft, attacking_aircraft, bombing_aircraft,
               aircraft_returned, aircraft_damaged, aircraft_lost):
        with db_session() as session:
            inserted_mission = MissionModel('15646444949', mission_date, airborne_aircraft, attacking_aircraft,
                                            bombing_aircraft,
                                            aircraft_returned, aircraft_damaged, aircraft_lost)
            session.add(inserted_mission)
            session.commit()

            return MissionInput(MissionInput=inserted_mission)
