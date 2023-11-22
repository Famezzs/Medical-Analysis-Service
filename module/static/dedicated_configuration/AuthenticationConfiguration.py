import os

class AuthenticationConfiguration:
    secret = os.environ.get("AUTH_SECRET")