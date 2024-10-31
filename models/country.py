from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from db import Base


class CountryModel(Base):
    __tablename__ = 'countries'

    country_id = Column(Integer, primary_key=True, autoincrement=True)
    country_name = Column(String(100), nullable=False, unique=True)

    cities = relationship("CityModel", back_populates="country")
