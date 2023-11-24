import datetime
from module.InputScanner import InputScanner
from module.OutputPrinter import OutputPrinter
from module.exception.ExceptionHandler import ExceptionHandler
from module.static.Configuration import Configuration
from module.data.entity.User import User
from module.helper.UserValidator import UserValidator

class MenuFunctions:
    @staticmethod
    def __get_user():
        input_scanner = InputScanner(OutputPrinter)
        name = input_scanner.scan('Name: ')
        sex = input_scanner.scan('Sex (M/F): ')
        birthday = input_scanner.scan('Birthday (YYYY-MM-DD): '); birthday = datetime.strptime(birthday, '%Y-%m-%d')
        user = User(); user.name = name; user.sex = sex; user.birthday = birthday
        user_validator = UserValidator(); user_validator.validate(user)
        return user

    @staticmethod
    def register():
        input_scanner = InputScanner(OutputPrinter)
        try:
            OutputPrinter.clear_console()
            user = MenuFunctions.__get_user()
        except Exception as e:
            exception_hander = ExceptionHandler(Configuration)
            exception_hander.handle(e)

    @staticmethod
    def exit_program():
        exit(0)
