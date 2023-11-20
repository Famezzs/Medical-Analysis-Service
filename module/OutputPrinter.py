import os
from module.abstract.ClearsConsole import ClearsConsole

class OutputPrinter(ClearsConsole):
    @staticmethod
    def print(output_string, additonal_next_line=False):
        print(output_string)
        if additonal_next_line == True:
            print()
    
    @staticmethod
    def clear_console():
        os.system('cls' if os.name == 'nt' else 'clear')