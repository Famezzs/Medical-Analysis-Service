from module.abstract.Validator import Validator

# Class which implements the validator pattern and is used
# for validating entity type
class TypeValidator(Validator):
    def validate(self, actual_type, expected_type):
        if not isinstance(actual_type, expected_type):
            raise TypeError('Invalid type passed')