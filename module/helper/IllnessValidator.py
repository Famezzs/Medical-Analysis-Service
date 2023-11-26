from module.abstract.Validator import Validator
from module.data.entity.Illness import Illness
from module.InputScanner import InputScanner
from module.exception.InvalidInput import InvalidInput

class IllnessValidator(Validator):
    def __init__(self, configuration):
        self.configuration = configuration

    def validate(self, illness: Illness, validate_not_exists = False):
        from module.controller.IllnessController import IllnessController
        if InputScanner.input_empty(illness.name):
            raise InvalidInput('Name cannot be empty or whitespace')
        if InputScanner.input_empty(illness.description):
            raise InvalidInput('Description cannot be empty or whitespace')
        if validate_not_exists:
            illness_controller = IllnessController(self.configuration)
            if illness_controller.get_illness(illness.name):
                raise InvalidInput('Illness with this login already exists')