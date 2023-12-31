from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from module.static.dedicated_configuration.EntityConfiguration import EntityConfiguration

# Class which represents login details table
class LoginDetails(EntityConfiguration.base):
    __tablename__ = 'login_details'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), unique=True)
    login = Column(String)
    password = Column(String)

    user = relationship("User", back_populates="login_details")