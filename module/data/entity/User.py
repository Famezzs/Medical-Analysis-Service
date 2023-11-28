from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from module.static.dedicated_configuration.EntityConfiguration import EntityConfiguration

# Class which represents users table
class User(EntityConfiguration.base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    birthday = Column(Date)
    sex = Column(String)

    patient = relationship("Patient", uselist=False, back_populates="user")
    doctor = relationship("Doctor", uselist=False, back_populates="user")
    login_details = relationship("LoginDetails", uselist=False, back_populates="user")