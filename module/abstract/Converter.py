from abc import ABC

# Abstract class which is implements the data converter pattern     
class Converter(ABC):
    def convert(self, *args, **kargs): ...