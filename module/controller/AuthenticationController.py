from module.abstract.Controller import Controller
from module.controller.UserController import UserController
from module.exception.Unauthorized import Unauthorized
from module.static.Configuration import Configuration
from module.data.entity.User import User
from module.data.entity.LoginDetails import LoginDetails
import bcrypt

class AuthenticationController(Controller):
    __current_session = None
    
    def __init__(self, configuration: Configuration):
        self.configuration = configuration

    @staticmethod
    def get_current_session():
        return AuthenticationController.__current_session
    
    @staticmethod
    def ensure_authenticated():
        if AuthenticationController.__current_session == None:
            raise Unauthorized('Unauthorized')
        
    def register_user(self, user: User, login_details: LoginDetails):
        user_controller = UserController(self.configuration)
        user_controller.create_user(user)
        login_details.password = self.hash_password(login_details.password)
        user_controller.create_login_details(login_details)
    
    def authenticate_user(self, login_details: LoginDetails):
        s

    def hash_password(self, password: str):
        password_bytes = password.encode('utf-8')
        secret_bytes = self.configuration.authentication_configuration.secret.encode('utf-8')

        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password_bytes + secret_bytes, salt)
    
        return hashed.decode('utf-8')

    def check_password(self, hash: str, password: str):
        password_bytes = password.encode('utf-8')
        secret_bytes = self.configuration.authentication_configuration.secret.encode('utf-8')

        return bcrypt.checkpw(password_bytes + secret_bytes, hash.encode('utf-8'))