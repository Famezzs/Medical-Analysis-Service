from module.abstract.Validator import Validator
from module.exception.InvalidInput import InvalidInput
from module.InputScanner import InputScanner

# Class which implements the validator pattern and is used
# for validating illnesses input during analysis
class IllnessesValidator(Validator):
    def validate(self, illnesses: str):
        if InputScanner.input_empty(illnesses):
            raise InvalidInput('Illnesses list cannot be empty or whitespace')     