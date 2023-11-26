from module.abstract.Controller import Controller
from module.data.entity.Illness import Illness
from module.helper.TypeValidator import TypeValidator
from module.exception.InvalidInput import InvalidInput

class IllnessController(Controller):
    def __init__(self, configuration):
        self.configuration = configuration
        from module.data.DatabaseEngine import DatabaseEngine
        self.database = DatabaseEngine(configuration)

    def __handle_illness_not_exists():
        raise InvalidInput('Illness specified does not exist')

    def __ensure_illness_exists(self, illness: Illness):
        TypeValidator.enforce_type(illness, Illness)
        if not self.database.query_records(Illness, Illness.name == illness.name):
            self.__handle_illness_not_exists()        

    def get_illness(self, name: str):
        TypeValidator.enforce_type(name, str)
        return self.database.query_records(Illness, Illness.name == name)
    
    def get_illnesses(self):
        return self.database.query_records(Illness)

    def create_illness(self, illness: Illness):
        from module.controller.AuthenticationController import AuthenticationController
        from module.controller.UserController import UserController
        from module.static.Configuration import Configuration
        TypeValidator.enforce_type(illness, Illness)
        AuthenticationController.ensure_authenticated()
        AuthenticationController.ensure_doctor()
        user_controller = UserController(Configuration); illness.creator_doctor_id = user_controller.get_doctor(AuthenticationController.get_current_session().user_id)[0].id
        return self.database.add_record(illness)
    
    def update_illness(self, updated_illness: Illness):
        from module.controller.AuthenticationController import AuthenticationController
        TypeValidator.enforce_type(updated_illness, Illness)
        AuthenticationController.ensure_authenticated()
        AuthenticationController.ensure_doctor()
        self.__ensure_illness_exists(updated_illness)
        return self.database.update_record(Illness, Illness.name == updated_illness.name, {Illness.description: updated_illness.description})
