from module.Menu import Menu
from module.OutputPrinter import OutputPrinter
from module.exception.ExceptionHandler import ExceptionHandler
from module.static.Configuration import Configuration

class Program:
    def run(self):
        OutputPrinter.clear_console()
        
        menu = Menu(Configuration)
        exceptionHandler = ExceptionHandler(Configuration)
        
        while True:
            try:
                menu.print_menu()
                menu.scan_and_invoke_option()
            except Exception as exception:
                exceptionHandler.handle(exception)