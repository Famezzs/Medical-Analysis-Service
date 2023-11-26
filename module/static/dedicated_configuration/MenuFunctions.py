import datetime
from module.InputScanner import InputScanner
from module.OutputPrinter import OutputPrinter
from module.data.entity.User import User
from module.data.entity.LoginDetails import LoginDetails
from module.data.entity.Illness import Illness
from module.helper.UserValidator import UserValidator
from module.helper.IllnessValidator import IllnessValidator
from module.helper.LoginDetailsValidator import LoginDetailsValidator
from module.controller.AuthenticationController import AuthenticationController
from module.controller.IllnessController import IllnessController
from datetime import datetime
import getpass

class MenuFunctions:
    @staticmethod
    def __get_user():
        input_scanner = InputScanner(OutputPrinter)
        name = input_scanner.scan('Name: ')
        sex = input_scanner.scan('Sex (M/F): ')
        birthday = input_scanner.scan('Birthday (YYYY-MM-DD): '); birthday = datetime.strptime(birthday, '%Y-%m-%d').date()
        user = User(); user.name = name; user.sex = sex; user.birthday = birthday
        user_validator = UserValidator(); user_validator.validate(user)
        return user

    @staticmethod
    def __get_login_details(validate_exists = False):
        from module.static.Configuration import Configuration
        input_scanner = InputScanner(OutputPrinter)
        login = input_scanner.scan('Login: ')
        password = getpass.getpass('Password: ')
        login_details = LoginDetails(); login_details.login = login; login_details.password = password
        login_details_validator = LoginDetailsValidator(Configuration); login_details_validator.validate(login_details, validate_exists)
        return login_details
    
    @staticmethod
    def __get_illness():
        from module.static.Configuration import Configuration
        input_scanner = InputScanner(OutputPrinter)
        name = input_scanner.scan('Name: ')
        description = input_scanner.scan('Description: ')
        illness = Illness(); illness.name = name; illness.description = description
        illness_validator = IllnessValidator(Configuration); illness_validator.validate(illness, True)
        return illness

    @staticmethod
    def register():
        from module.static.Configuration import Configuration
        OutputPrinter.clear_console()
        login_details = MenuFunctions.__get_login_details(True)
        OutputPrinter.clear_console() 
        user = MenuFunctions.__get_user()
        authentication_controller = AuthenticationController(Configuration); authentication_controller.register_user(user, login_details)

    @staticmethod
    def login():
        from module.static.Configuration import Configuration
        OutputPrinter.clear_console(); 
        login_details = MenuFunctions.__get_login_details()
        authentication_controller = AuthenticationController(Configuration); authentication_controller.authenticate_user(login_details)

    @staticmethod
    def logout():
        from module.static.Configuration import Configuration
        OutputPrinter.clear_console()
        authentication_controller = AuthenticationController(Configuration); authentication_controller.logout_user()

    @staticmethod
    def create_illness():
        from module.static.Configuration import Configuration
        OutputPrinter.clear_console()
        illness = MenuFunctions.__get_illness()
        OutputPrinter.clear_console()
        Illness_controller = IllnessController(Configuration); Illness_controller.create_illness(illness)

    @staticmethod
    def exit_program():
        exit(0)