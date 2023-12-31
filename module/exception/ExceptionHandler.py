# Class which used used for exception handling
class ExceptionHandler:
    def __init__(self, configuration):
        self.printer = configuration.exception_handler_configuration.printer
    
    def handle(self, exception):
        self.printer.clear_console()
        self.printer.print(exception, True)
        input('Press Enter to continue...')
        self.printer.clear_console()