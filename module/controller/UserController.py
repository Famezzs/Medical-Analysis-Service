from module.abstract.Controller import Controller
from module.data.DatabaseEngine import DatabaseEngine
from module.data.entity.User import User
from module.data.entity.Patient import Patient
from module.data.entity.Doctor import Doctor
from module.data.entity.LoginDetails import LoginDetails
from module.helper.TypeValidator import TypeValidator

# Class which is used for providing CRUD operations over user entity records
class UserController(Controller):
    def __init__(self, configuration):
        self.configuration = configuration
        self.database = DatabaseEngine(configuration)

    def create_user(self, user: User):
        TypeValidator.enforce_type(user, User)
        return self.database.add_record(user)

    def create_patient(self, patient: Patient):
        TypeValidator.enforce_type(patient, Patient)
        self.database.add_record(patient)

    def get_login_details(self, login: str):
        TypeValidator.enforce_type(login, str)
        return self.database.query_records(LoginDetails, filter_condition=(LoginDetails.login == login))
    
    def create_login_details(self, login_details: LoginDetails):
        TypeValidator.enforce_type(login_details, LoginDetails)
        self.database.add_record(login_details)

    def get_doctor(self, user_id: int):
        TypeValidator.enforce_type(user_id, int)
        return self.database.query_records(Doctor, Doctor.user_id == user_id)