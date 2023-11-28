from module.Menu import Menu
from module.exception.ExceptionHandler import ExceptionHandler
from module.static.Configuration import Configuration

# Function which implements the runtime program
class Program:
    def run(self):        
        menu = Menu(Configuration)
        exceptionHandler = ExceptionHandler(Configuration)
        while True:
            try:
                menu.print_menu()
                menu.scan_and_invoke_option()
            except Exception as exception:
                exceptionHandler.handle(exception)