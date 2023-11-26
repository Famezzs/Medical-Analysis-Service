from module.abstract.Controller import Controller
from module.data.DatabaseEngine import DatabaseEngine
from module.data.entity.Illness import Illness
from module.helper.TypeValidator import TypeValidator

class IllnessController(Controller):
    def __init__(self, configuration):
        self.configuration = configuration
        self.database = DatabaseEngine(configuration)

    def get_illness(self, name: str):
        TypeValidator.enforce_type(name, str)
        return self.database.query_records(Illness, Illness.name == name)
    
    def get_illnesses(self):
        return self.database.query_records(Illness)

    def create_illness(self, illness: Illness):
        from module.controller.AuthenticationController import AuthenticationController
        TypeValidator.enforce_type(illness, Illness)
        AuthenticationController.ensure_authenticated()
        AuthenticationController.ensure_doctor(self.configuration)
        return self.database.add_record(illness)
    
    def update_illness(self, updated_illness: Illness):
        from module.controller.AuthenticationController import AuthenticationController
        TypeValidator.enforce_type(updated_illness, Illness)
        AuthenticationController.ensure_authenticated()
        AuthenticationController.ensure_doctor(self.configuration)
        return self.database.update_record(Illness, Illness.id == updated_illness.name or Illness.name == updated_illness.name, updated_illness)
