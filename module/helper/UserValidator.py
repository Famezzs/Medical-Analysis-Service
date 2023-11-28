import datetime
from module.abstract.Validator import Validator
from module.data.entity.User import User
from module.InputScanner import InputScanner
from module.exception.EmptyInput import EmptyInput
from module.exception.InvalidInput import InvalidInput
from datetime import datetime

# Class which implements the validator pattern and is used
# for validating user entity input
class UserValidator(Validator):
    def validate(self, user: User):
        if InputScanner.input_empty(user.name):
            raise EmptyInput('Name cannot be empty or whitespace')
        if user.sex != 'M' and user.sex != 'F':
            raise InvalidInput("Sex can only be specified as 'M' and 'F'")
        if user.birthday > datetime.now().date() or user.birthday == datetime.now().date():
            raise InvalidInput('Date cannot be in the future or represent current date')