from module.static.dedicated_configuration.DatabaseConfiguration import DatabaseConfiguration
from module.static.dedicated_configuration.ExceptionHandlerConfiguration import ExceptionHandlerConfiguration
from module.static.dedicated_configuration.MenuConfiguration import MenuConfiguration
from module.static.dedicated_configuration.AuthenticationConfiguration import AuthenticationConfiguration

# Class which stores the application's configuration
class Configuration:
    database_configuration = DatabaseConfiguration
    exception_handler_configuration = ExceptionHandlerConfiguration
    menu_configuration = MenuConfiguration
    authentication_configuration = AuthenticationConfiguration