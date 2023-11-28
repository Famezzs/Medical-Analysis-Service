from module.exception.EmptyInput import EmptyInput

# Class which implements the input functionality of the application
class InputScanner():
    def __init__(self, printer):
        self.printer = printer

    def scan(self, prompt='', allow_empty=False):
        input_string = input(prompt)
        
        if allow_empty == False and InputScanner.input_empty(input_string) == True:
            raise EmptyInput('Input cannot be empty')
        
        return input_string
        
    @staticmethod
    def input_empty(input_string):
        return input_string == "" or input_string.isspace() == True