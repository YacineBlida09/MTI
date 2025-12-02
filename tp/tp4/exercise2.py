#Create a simple MVC implementation where the user inputs their name, and the application displays a greeting message.

class UserModel:    
    def __init__(self):
        self.name = ""

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

class UserView:
    def get_user_input(self):
        return input("Donner votre nom: ")

    def display_greeting(self, name):
        print(f"Bonjour, {name}! Bienvenue dans l'exemple MVC.")

class UserController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def run(self):
        name = self.view.get_user_input()
        self.model.set_name(name)
        self.view.display_greeting(self.model.get_name())
    

model = UserModel()
view = UserView()
controller = UserController(model, view)
controller.run()
