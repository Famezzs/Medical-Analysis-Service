import os

# Class which specifies how the AuthenticationController class instance should behave
class AuthenticationConfiguration:
    secret = os.environ.get("AUTH_SECRET")