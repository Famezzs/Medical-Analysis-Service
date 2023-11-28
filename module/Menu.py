from module.abstract.ClearsConsole import ClearsConsole
from module.exception.InvalidOption import InvalidOption

# Class which is used for rendering the appliaction's menu
class Menu(ClearsConsole):
    def __init__(self, configuration):
        self.options_and_descriptions = configuration.menu_configuration.options_and_descriptions
        self.options_and_functions = configuration.menu_configuration.options_and_functions
        self.options_and_conditions = configuration.menu_configuration.options_and_conditions
        self.scanner = configuration.menu_configuration.scanner
        self.printer = configuration.menu_configuration.printer

    def option_present(self, option):
        return option in self.options_and_functions

    def invoke_function(self, option):
        if self.option_present(option) == False or self.options_and_conditions[option]() == False:
            raise InvalidOption('Invalid option specified')
        self.options_and_functions[option]()
    
    def print_menu(self):
        self.printer.clear_console()
        for option in list(self.options_and_descriptions.keys()):
            if option == '0':
                self.printer.print('')
            if self.options_and_conditions[option]():
                self.printer.print('[' + option + '] - ' + self.options_and_descriptions[option])
            else:
                self.printer.print_colored('[' + option + '] - ' + self.options_and_descriptions[option], 'grey')
        self.printer.print('')

    def scan_and_invoke_option(self):
        option = self.scanner.scan()
        self.printer.clear_console()
        self.invoke_function(option)