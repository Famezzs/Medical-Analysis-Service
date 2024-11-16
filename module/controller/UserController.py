from module.abstract.Controller import Controller
from module.data.DatabaseEngine import DatabaseEngine
from module.data.entity.User import User
from module.data.entity.Patient import Patient
from module.data.entity.Doctor import Doctor
from module.data.entity.LoginDetails import LoginDetails
from module.helper.TypeValidator import TypeValidator
from module.helper.UserValidator import UserValidator

# Class which is used for providing CRUD operations over user entity records
class UserController(Controller):
    def __init__(self, configuration):
        self.configuration = configuration
        self.database = DatabaseEngine(configuration)

    @staticmethod
    def parse_json_user(user_json_data):
        from datetime import datetime
        user = User(
            name=user_json_data.get('name'),
            birthday=datetime.strptime(user_json_data.get('birthday'), '%Y-%m-%d').date(),
            sex=user_json_data.get('sex')
        )
        user_validator = UserValidator(); user_validator.validate(user)
        return user

    def create_user(self, user: User):
        type_validator = TypeValidator(); type_validator.validate(user, User)
        return self.database.add_record(user)

    def create_patient(self, patient: Patient):
        type_validator = TypeValidator(); type_validator.validate(patient, Patient)
        self.database.add_record(patient)

    def get_login_details(self, login: str):
        type_validator = TypeValidator(); type_validator.validate(login, str)
        return self.database.query_records(LoginDetails, filter_condition=(LoginDetails.login == login))
    
    def create_login_details(self, login_details: LoginDetails):
        type_validator = TypeValidator(); type_validator.validate(login_details, LoginDetails)
        self.database.add_record(login_details)

    def get_doctor(self, user_id: int):
        type_validator = TypeValidator(); type_validator.validate(user_id, int)
        return self.database.query_records(Doctor, Doctor.user_id == user_id)