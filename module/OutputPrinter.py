import os
from module.abstract.ClearsConsole import ClearsConsole
from termcolor import colored

# Class which implements the printing functionality used by application
class OutputPrinter(ClearsConsole):
    @staticmethod
    def print(output_string, additional_next_line=False, no_new_line=False):
        if no_new_line == True:
            print(output_string, end='')
        else:
            print(output_string)
        if additional_next_line == True:
            print()

    @staticmethod
    def print_colored(output_string, color, additional_next_line=False):
        print(colored(output_string, color))
        if additional_next_line == True:
            print()
    
    @staticmethod
    def clear_console():
        os.system('cls' if os.name == 'nt' else 'clear')