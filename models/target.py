from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db import Base

class TargetModel(Base):
    __tablename__ = 'targets'

    target_id = Column(Integer, primary_key=True, autoincrement=True)
    mission_id = Column(Integer, ForeignKey('missions.mission_id'))
    target_industry = Column(String(255), nullable=False)
    city_id = Column(Integer, ForeignKey('cities.city_id'))
    target_type_id = Column(Integer, ForeignKey('targettypes.target_type_id'))
    target_priority = Column(Integer)

    mission = relationship('MissionModel', back_populates='targets')
    city = relationship('CityModel', back_populates='targets')
    target_type = relationship('TargetTypeModel', back_populates='targets')