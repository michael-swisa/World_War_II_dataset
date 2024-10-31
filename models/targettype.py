from sqlalchemy.orm import relationship
from db import Base
from sqlalchemy import Column, Integer, String


class TargetTypeModel(Base):
    __tablename__ = 'targettypes'

    target_type_id = Column(Integer, primary_key=True, autoincrement=True)
    target_type_name = Column(String(255), nullable=False)

    targets = relationship('TargetModel', back_populates='target_type')
