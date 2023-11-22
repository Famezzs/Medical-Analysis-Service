from module.abstract.Controller import Controller
from module.controller.AuthenticationController import AuthenticationController
from module.static.Configuration import Configuration
from module.data.DatabaseEngine import DatabaseEngine
from module.data.entity.User import User
from module.data.entity.Patient import Patient
from module.data.entity.Doctor import Doctor
from module.data.entity.Administrator import Administrator
from module.data.entity.LoginDetails import LoginDetails

class UserController(Controller):
    def __init__(self, configuration: Configuration):
        self.configuration = configuration
        self.database = DatabaseEngine(configuration)

    def __enforce_type(self, actual_type, expected_type):
        if not isinstance(actual_type, expected_type):
            raise TypeError('Invalid type passed')
        
    def __is_user_administrator(self, user: User):
        administrator = self.database.query_records(Administrator, Administrator.user_id == user.id)
        if administrator:
            return True
        else:
            return False

    def create_user(self, user: User):
        self.__enforce_type(user, User)
        self.database.add_record(user)

    def create_patient(self, patient: Patient):
        self.__enforce_type(patient, Patient)
        self.database.add_record(patient)

    def create_doctor(self, doctor: Doctor):
        self.__enforce_type(doctor, Doctor)
        AuthenticationController.ensure_authenticated()
        self.__is_user_administrator(AuthenticationController.get_current_session())
        self.database.add_record(doctor)

    def create_login_details(self, login_details: LoginDetails):
        self.__enforce_type(login_details, LoginDetails)
        self.database.add_record(login_details)