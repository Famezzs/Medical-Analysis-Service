from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

class LoginDetails(Base):
    __tablename__ = 'login_details'

    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    login = Column(String)
    password = Column(String)

    user = relationship("User", back_populates="login_detail")