from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship

class User(declarative_base()):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    birthday = Column(Date)
    sex = Column(String)

    # Relationships
    patient = relationship("Patient", uselist=False, back_populates="user")
    doctor = relationship("Doctor", uselist=False, back_populates="user")
    login_details = relationship("LoginDetails", uselist=False, back_populates="user")