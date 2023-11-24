from abc import ABC
    
class Validator(ABC):
    def validate(self, to_validate): ...