from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from module.static.dedicated_configuration.EntityConfiguration import EntityConfiguration

class Doctor(EntityConfiguration.base):
    __tablename__ = 'doctors'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)

    user = relationship("User", back_populates="doctor")