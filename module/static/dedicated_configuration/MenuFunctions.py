import datetime
from module.InputScanner import InputScanner
from module.OutputPrinter import OutputPrinter
from module.data.entity.User import User
from module.data.entity.LoginDetails import LoginDetails
from module.data.entity.Illness import Illness
from module.helper.UserValidator import UserValidator
from module.helper.IllnessValidator import IllnessValidator
from module.helper.IllnessesValidator import IllnessesValidator
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
    def __get_illness(validate_not_exists = False, validate_description_changed = False):
        from module.static.Configuration import Configuration
        input_scanner = InputScanner(OutputPrinter)
        name = input_scanner.scan('Name: ')
        description = input_scanner.scan('Description: ')
        illness = Illness(); illness.name = name; illness.description = description
        illness_validator = IllnessValidator(Configuration); illness_validator.validate(illness, validate_not_exists, validate_description_changed)
        return illness
    
    @staticmethod
    def __print_illnesses_names(illnesses: list):
        OutputPrinter.print('Available illnesses:')
        size_of_illnesses_list = len(illnesses)
        for i in range(size_of_illnesses_list):
            if i < size_of_illnesses_list - 1:
                OutputPrinter.print(illnesses[i].name + ', ', False, True)
            else:
                OutputPrinter.print(illnesses[i].name, True)

    @staticmethod
    def __get_illnesses():
        input_scanner = InputScanner(OutputPrinter)
        illnesses = input_scanner.scan('Illnesses for analysis (enter a comma separated list): ')
        illnesses_validator = IllnessesValidator(); illnesses_validator.validate(illnesses)
        return illnesses
    
    @staticmethod
    def __illnesses_string_to_list(illnesses: str):
        illnesses_list = illnesses.split(',')
        for i in range(len(illnesses_list)):
            illnesses_list[i] = illnesses_list[i].strip()
        return illnesses_list
    
    @staticmethod
    def __output_analysis(illnesses: list):
        if illnesses:
            for illness in illnesses:
                OutputPrinter.print(illness.name)
                OutputPrinter.print(illness.description, True)
        else:
            OutputPrinter.print('No records found')

    @staticmethod
    def __await_user_input():
        input('Press Enter to continue...')

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
        illness = MenuFunctions.__get_illness(True, False)
        OutputPrinter.clear_console()
        Illness_controller = IllnessController(Configuration); Illness_controller.create_illness(illness)

    @staticmethod
    def update_illness():
        from module.static.Configuration import Configuration
        OutputPrinter.clear_console()
        illness = MenuFunctions.__get_illness(False, True)
        OutputPrinter.clear_console()
        illness_controller = IllnessController(Configuration); illness_controller.update_illness(illness)

    @staticmethod
    def conduct_analysis():
        from module.static.Configuration import Configuration
        OutputPrinter.clear_console()
        illness_controller = IllnessController(Configuration); illnesses = illness_controller.get_illnesses()
        MenuFunctions.__print_illnesses_names(illnesses)
        requested_illnesses_string = MenuFunctions.__get_illnesses()
        requested_illnesses_list = MenuFunctions.__illnesses_string_to_list(requested_illnesses_string)
        requested_illnesses = illness_controller.get_illnesses_from_list(requested_illnesses_list)
        OutputPrinter.clear_console()
        MenuFunctions.__output_analysis(requested_illnesses)
        MenuFunctions.__await_user_input()
        OutputPrinter.clear_console()

    @staticmethod
    def exit_program():
        exit(0)