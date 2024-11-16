from abc import ABC

# Abstract class which is implements the data validator pattern     
class Validator(ABC):
    def validate(self, *args, **kargs): ...