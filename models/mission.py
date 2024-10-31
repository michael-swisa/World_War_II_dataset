from sqlalchemy import Column, Integer, Date, Numeric
from sqlalchemy.orm import relationship
from db import Base


class MissionModel(Base):
    __tablename__ = 'missions'

    mission_id = Column(Integer, primary_key=True)
    mission_date = Column(Date)
    airborne_aircraft = Column(Numeric)
    attacking_aircraft = Column(Numeric)
    bombing_aircraft = Column(Numeric)
    aircraft_returned = Column(Numeric)
    aircraft_failed = Column(Numeric)
    aircraft_damaged = Column(Numeric)
    aircraft_lost = Column(Numeric)

    targets = relationship("TargetModel", back_populates="mission")