from module.InputScanner import InputScanner
from module.OutputPrinter import OutputPrinter
from module.static.dedicated_configuration.MenuFunctions import MenuFunctions

class MenuConfiguration:
    options_and_functions = {
        '1': MenuFunctions.register,
        '0': MenuFunctions.exit_program
    }

    options_and_descriptions = {
        '1': 'Register',
        '2': 'Log In',
        '': '',
        '0': 'Exit'
    }

    scanner = InputScanner(OutputPrinter)

    printer = OutputPrinter

