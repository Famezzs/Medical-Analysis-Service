import os
from module.data.entity.User import User
from module.data.entity.Patient import Patient 
from module.data.entity.Doctor import Doctor
from module.data.entity.LoginDetails import LoginDetails
from module.data.entity.Illness import Illness 
from module.OutputPrinter import OutputPrinter

# Class which specifies how the DatabaseEngine class instance should behave
class DatabaseConfiguration:
    connection_string = os.environ.get("DB_CONNECTION")
    entities = [User, Patient, Doctor, LoginDetails, Illness]
    printer = OutputPrinter