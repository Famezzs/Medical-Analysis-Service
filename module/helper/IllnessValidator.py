from module.abstract.Validator import Validator
from module.data.entity.Illness import Illness
from module.InputScanner import InputScanner
from module.exception.InvalidInput import InvalidInput

# Class which implements the validator pattern and is used
# for validating illness entity input
class IllnessValidator(Validator):
    def __init__(self, configuration):
        self.configuration = configuration

    def validate(self, illness: Illness, validate_not_exists = False, validate_description_changed = False):
        from module.controller.IllnessController import IllnessController
        if InputScanner.input_empty(illness.name):
            raise InvalidInput('Name cannot be empty or whitespace')
        if InputScanner.input_empty(illness.description):
            raise InvalidInput('Description cannot be empty or whitespace')
        if validate_not_exists:
            illness_controller = IllnessController(self.configuration)
            if illness_controller.get_illness(illness.name):
                raise InvalidInput('Illness with this name already exists')
        else:
            illness_controller = IllnessController(self.configuration)
            if not illness_controller.get_illness(illness.name):
                raise InvalidInput('Specified illness does not exist')
        if validate_description_changed:
            illness_controller = IllnessController(self.configuration)
            if illness_controller.get_illness(illness.name)[0].description == illness.description:
                raise InvalidInput('Description should differ')