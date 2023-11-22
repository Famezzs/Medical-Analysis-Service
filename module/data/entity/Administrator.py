from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

class Administrator(Base):
    __tablename__ = 'administrators'

    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)

    user = relationship("User", back_populates="administrator")