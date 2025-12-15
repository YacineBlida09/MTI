# File: python/tp/tp5/exercice1.py
class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

class UserSaver:
    def save(self, user):
        # Database logic 
        pass

class EmailService:
    def send_welcome_email(self, user):
        # Email logic here
        pass

class ReportService:
    def generate_report(self, users):
        # Reporting logic here
        pass
