from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from module.static.dedicated_configuration.EntityConfiguration import EntityConfiguration

class Illness(EntityConfiguration.base):
    __tablename__ = 'illnesses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    creator_doctor_id = Column(Integer, ForeignKey('doctors.id'))

    doctor = relationship("Doctor", back_populates="illness")