from module.static.Configuration import Configuration
from module.abstract.ClearsConsole import ClearsConsole
from module.exception.InvalidOption import InvalidOption

class Menu(ClearsConsole):
    def __init__(self, configuration: Configuration):
        self.options_and_descriptions = configuration.menu_configuration.options_and_descriptions
        self.options_and_functions = configuration.menu_configuration.options_and_functions
        self.scanner = configuration.menu_configuration.scanner
        self.printer = configuration.menu_configuration.printer

    def option_present(self, option):
        return option in self.options_and_functions

    def invoke_function(self, option):
        if self.option_present(option) == True:
            self.options_and_functions[option]()
        else:
            raise InvalidOption('Invalid option specified')
    
    def print_menu(self):
        for option in list(self.options_and_descriptions.keys()):
            self.printer.print('[' + option + '] - ' + self.options_and_descriptions[option])
        self.printer.print('')

    def scan_and_invoke_option(self):
        option = self.scanner.scan()
        self.printer.clear_console()
        self.invoke_function(option)
    