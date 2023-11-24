from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from module.static.dedicated_configuration.EntityConfiguration import EntityConfiguration

class Patient(EntityConfiguration.base):
    __tablename__ = 'patients'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)

    user = relationship("User", back_populates="patient")