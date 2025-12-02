class UserModel:
    def __init__(self):
        self.__name = ""
    
    def set_name(self, name):
        self.__name = name
    
    def get_name(self):
        return self.__name
    
class UserView:
    def get_user_input(self):
        return input("donner le nom d utilisateur\n")
    
    def user_output(self, name):
        print (f"bnj {name} cv?")

class UserController:
    def __init__(self, model, view):
        self.__model = model
        self.__view = view
    
    def run(self):
        name = self.__view.get_user_input()
        self.__model.set_name(name)
        name = self.__model.get_name()
        self.__view.user_output(name)


model = UserModel()
view = UserView()
controller = UserController (model, view)
controller.run()

