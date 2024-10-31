from sqlalchemy import Column, Integer, ForeignKey, Numeric, String
from sqlalchemy.orm import relationship
from db import Base


class CityModel(Base):
    __tablename__ = 'cities'

    city_id = Column(Integer, primary_key=True, autoincrement=True)
    city_name = Column(String(100), nullable=False)
    country_id = Column(Integer, ForeignKey('countries.country_id'), nullable=False)
    latitude = Column(Numeric, nullable=False)
    longitude = Column(Numeric, nullable=False)

    country = relationship('CountryModel', back_populates='cities')
    targets = relationship('TargetModel', back_populates='city')


