from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

class Doctor(Base):
    __tablename__ = 'doctors'

    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)

    # Relationship to User
    user = relationship("User", back_populates="doctor")