import re

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class LoginInterface:
    def __init__(self):
        self.user = None
        self.logged_in = False

    def validate_username(self, username):
        if len(username) < 5:
            return False
        if not re.match("^[A-Za-z0-9]+$", username):
            return False
        return True

    def validate_password(self, password):
        if len(password) < 8:
            return False
        if not re.search("[a-z]", password):
            return False
        if not re.search("[A-Z]", password):
            return False
        if not re.search("[0-9]", password):
            return False
        return True

    def register(self, username, password):
        if not self.validate_username(username):
            return "Invalid username."
        if not self.validate_password(password):
            return "Invalid password."
        self.user = User(username, password)
        return "User created successfully."

    def login(self, username, password):
        if not self.validate_username(username):
            return "Invalid username."
        if not self.validate_password(password):
            return "Invalid password."
        if username != self.user.username or password != self.user.password:
            return "Invalid username or password."
        self.logged_in = True
        return "Logged in successfully."

    def logout(self):
        if not self.logged_in:
            return "User is not logged in."
        self.logged_in = False
        return "Logged out successfully."