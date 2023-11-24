from module.abstract.Validator import Validator
from module.data.entity.LoginDetails import LoginDetails
from module.controller.UserController import UserController
from module.static.Configuration import Configuration
from module.InputScanner import InputScanner
from module.exception.InvalidInput import InvalidInput
import re

class LoginDetailsValidator(Validator):
    def __init__(self, configuration: Configuration):
        self.configuration = configuration

    def __check_login_secure(self, login: str):
        if len(login) < 6:
            return False
        else:
            return True
    
    def __check_password_secure(self, password: str):
        if len(password) < 8:
            return False
        if not re.search("[A-Z]", password):
            return False
        if not re.search("[a-z]", password):
            return False
        if not re.search("[0-9]", password):
            return False
        if not re.search("[!@#$%^&*(),.?\":{}|<>]", password):
            return False
        return True

    def validate(self, login_details: LoginDetails):
        if InputScanner.input_empty(login_details.login):
            raise InvalidInput('Login cannot be empty or whitespace')
        if InputScanner.input_empty(login_details.password):
            raise InvalidInput('Password cannot be empty or whitespace')
        if self.__check_login_secure(login_details.login):
            raise InvalidInput('Login must contain more than 5 characters')
        if self.__check_password_secure(login_details.password):
            raise InvalidInput('Password must contain more than 7 characters')
        user_controller = UserController(self.configuration)
        if user_controller.get_login_details(login_details.login):
            raise 