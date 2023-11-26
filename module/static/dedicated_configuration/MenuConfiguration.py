from module.InputScanner import InputScanner
from module.OutputPrinter import OutputPrinter
from module.static.dedicated_configuration.MenuFunctions import MenuFunctions

class MenuConfiguration:
    options_and_functions = {
        '1': MenuFunctions.register,
        '2': MenuFunctions.login,
        '3': MenuFunctions.logout,
        '4': MenuFunctions.conduct_analysis,
        '5': MenuFunctions.create_illness,
        '6': MenuFunctions.update_illness,
        '0': MenuFunctions.exit_program
    }

    options_and_descriptions = {
        '1': 'Register',
        '2': 'Log In',
        '3': 'Log Out',
        '4': 'Conduct Analysis',
        '5': 'Create Illness',
        '6': 'Update Illness',
        '0': 'Exit'
    }

    options_and_conditions = {
        '1': lambda: __import__('module.controller.AuthenticationController', fromlist=['AuthenticationController']).AuthenticationController.is_authenticated() == False,
        '2': lambda: __import__('module.controller.AuthenticationController', fromlist=['AuthenticationController']).AuthenticationController.is_authenticated() == False,
        '3': lambda: __import__('module.controller.AuthenticationController', fromlist=['AuthenticationController']).AuthenticationController.is_authenticated() == True,
        '4': lambda: __import__('module.controller.AuthenticationController', fromlist=['AuthenticationController']).AuthenticationController.is_authenticated() == True,
        '5': lambda: __import__('module.controller.AuthenticationController', fromlist=['AuthenticationController']).AuthenticationController.is_doctor() == True,
        '6': lambda: __import__('module.controller.AuthenticationController', fromlist=['AuthenticationController']).AuthenticationController.is_doctor() == True,
        '0': lambda: True
    }

    scanner = InputScanner(OutputPrinter)

    printer = OutputPrinter

