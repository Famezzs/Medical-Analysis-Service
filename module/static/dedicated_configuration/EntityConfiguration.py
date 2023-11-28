from sqlalchemy.ext.declarative import declarative_base

# Class which specifies what the entity classes use for inheritance
class EntityConfiguration:
    base = declarative_base()