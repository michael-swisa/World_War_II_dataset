from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from models.target import TargetModel
from models.mission import MissionModel
from models.city import CityModel
from models.targettype import TargetTypeModel
from models.country import CountryModel