from module.abstract.Controller import Controller
from module.data.DatabaseEngine import DatabaseEngine
from module.data.entity.User import User
from module.data.entity.Patient import Patient
from module.data.entity.LoginDetails import LoginDetails

class UserController(Controller):
    def __init__(self, configuration):
        self.configuration = configuration
        self.database = DatabaseEngine(configuration)

    def __enforce_type(self, actual_type, expected_type):
        if not isinstance(actual_type, expected_type):
            raise TypeError('Invalid type passed')

    def create_user(self, user: User):
        self.__enforce_type(user, User)
        return self.database.add_record(user)

    def create_patient(self, patient: Patient):
        self.__enforce_type(patient, Patient)
        self.database.add_record(patient)

    def create_login_details(self, login_details: LoginDetails):
        self.__enforce_type(login_details, LoginDetails)
        self.database.add_record(login_details)

    def get_login_details(self, login: str):
        self.__enforce_type(login, str)
        return self.database.query_records(LoginDetails, filter_condition=(LoginDetails.login == login))