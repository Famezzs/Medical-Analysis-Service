from module.InputScanner import InputScanner
from module.OutputPrinter import OutputPrinter
from module.static.dedicated_configuration.MenuFunctions import MenuFunctions

class MenuConfiguration:
    options_and_functions = {
        '1': MenuFunctions.register,
        '2': MenuFunctions.login,
        '3': MenuFunctions.logout,
        '0': MenuFunctions.exit_program
    }

    options_and_descriptions = {
        '1': 'Register',
        '2': 'Log In',
        '3': 'Log Out',
        '0': 'Exit'
    }

    options_and_conditions = {
        '1': lambda: __import__('module.controller.AuthenticationController', fromlist=['AuthenticationController']).AuthenticationController.is_authenticated() == False,
        '2': lambda: __import__('module.controller.AuthenticationController', fromlist=['AuthenticationController']).AuthenticationController.is_authenticated() == False,
        '3': lambda: __import__('module.controller.AuthenticationController', fromlist=['AuthenticationController']).AuthenticationController.is_authenticated() == True,
        '0': lambda: True
    }

    scanner = InputScanner(OutputPrinter)

    printer = OutputPrinter

