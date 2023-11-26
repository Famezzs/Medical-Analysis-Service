from module.abstract.Controller import Controller
from module.exception.Unauthorized import Unauthorized
from module.data.entity.User import User
from module.data.entity.LoginDetails import LoginDetails
from module.exception.LoginFailed import LoginFailed
import bcrypt

class AuthenticationController(Controller):
    __current_session = None
    
    def __init__(self, configuration):
        self.configuration = configuration

    def __hash_password(self, password: str):
        password_bytes = password.encode('utf-8')
        secret_bytes = self.configuration.authentication_configuration.secret.encode('utf-8')

        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password_bytes + secret_bytes, salt)
    
        return hashed.decode('utf-8')

    def __check_password(self, hash: str, password: str):
        password_bytes = password.encode('utf-8')
        secret_bytes = self.configuration.authentication_configuration.secret.encode('utf-8')

        return bcrypt.checkpw(password_bytes + secret_bytes, hash.encode('utf-8'))

    def __get_login_details(self, login: str):
        from module.controller.UserController import UserController
        user_controller = UserController(self.configuration)
        stored_login_details = user_controller.get_login_details(login)
        if not stored_login_details:
            raise LoginFailed('Login failed')
        else:
            return stored_login_details

    def __compare_login_details(self, stored_login_details: LoginDetails, provided_login_details: LoginDetails):
        match = self.__check_password(stored_login_details.password, provided_login_details.password)
        if match == False:
            raise LoginFailed('Login failed')
        
    @staticmethod
    def __handle_unauthorized():
        raise Unauthorized('You are unauthorized to perform this action')

    @staticmethod
    def get_current_session():
        return AuthenticationController.__current_session
    
    @staticmethod
    def is_authenticated():
        return AuthenticationController.__current_session != None
    
    @staticmethod
    def ensure_authenticated():
        if AuthenticationController.__current_session == None:
            AuthenticationController.__handle_unauthorized()
        
    @staticmethod
    def is_doctor():
        if AuthenticationController.is_authenticated() == False:
            return False
        from module.controller.UserController import UserController
        from module.static.Configuration import Configuration
        user_controller = UserController(Configuration)
        if user_controller.get_doctor(AuthenticationController.__current_session.user_id):
            return True
        else:
            return False

    @staticmethod
    def ensure_doctor():
        from module.controller.UserController import UserController
        from module.static.Configuration import Configuration
        user_controller = UserController(Configuration)
        if AuthenticationController.is_authenticated() == False or not user_controller.get_doctor(AuthenticationController.__current_session.user_id):
            AuthenticationController.__handle_unauthorized()

    def register_user(self, user: User, login_details: LoginDetails):
        from module.controller.UserController import UserController
        user_controller = UserController(self.configuration)
        login_details.password = self.__hash_password(login_details.password)
        login_details.user_id = user_controller.create_user(user)
        user_controller.create_login_details(login_details)
    
    def authenticate_user(self, login_details: LoginDetails):
        stored_login_details = self.__get_login_details(login_details.login)[0]
        self.__compare_login_details(stored_login_details, login_details)
        AuthenticationController.__current_session = stored_login_details
    
    def logout_user(self):
        AuthenticationController.__current_session = None