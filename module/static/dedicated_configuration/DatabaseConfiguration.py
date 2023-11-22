import os
from module.data.entity.User import User
from module.data.entity.Patient import Patient 
from module.data.entity.Doctor import Doctor
from module.data.entity.Administrator import Administrator
from module.data.entity.LoginDetails import LoginDetails 
from module.OutputPrinter import OutputPrinter

class DatabaseConfiguration:
    connection_string = os.environ.get("DB_CONNECTION")
    entities = [User, Patient, Doctor, Administrator, LoginDetails]
    printer = OutputPrinter