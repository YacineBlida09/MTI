#:Build a Task Manager using MVC. The application allows the user to add, view, update, and delete tasks.
# Tasks should have a title, description, and status (e.g., "To Do," "In Progress," "Completed").

class TaskModel:
    def __init__(self):
        self.__title = ""
        self.__description = ""
        self.__status = ""
    
    def update(self, title, description, status):
        self.__title = title
        self.__description = description
        self.__status = status
    
    def get_title(self):
        return self.__title
    
    def get_description(self):
        return self.__description

    def get_status(self):
        return self.__status

    def delete(self):
        self.__title = ""
        self.__description = ""
        self.__status = ""


class TaskView:
    def infos(self, task):
        print(f"Titre: {task.get_title()}")
        print(f"Description: {task.get_description()}")
        print(f"Status: {task.get_status()}")

    def ask(self):
        return input("Donner un titre, description et etat a votre task dans cet ordre separés par un espace\n").split()
    
class TaskController:
    def __init__(self, view):
        self.tasks = []
        self.view = view

    def run(self):
        while True:
            action = input("\nChoisir une action: [a]jouter, [v]oir, [s]upprimer, [q]uitter: ").lower()
            
            if action == 'a':
                t, d, s = self.view.ask()
                task = TaskModel()
                task.update(t, d, s)
                self.tasks.append(task)
            
            elif action == 'v':
                if not self.tasks:
                    print("Aucune tâche enregistree.")
                else:
                    for i, task in enumerate(self.tasks, 1):
                        print(f"\nTâche {i}:")
                        self.view.infos(task)
            
            elif action == 's':
                if not self.tasks:
                    print("Aucune tache a supprimer.")
                else:
                    index = int(input("Numero de la tache a supprimer: ")) - 1
                    if 0 <= index < len(self.tasks):
                        self.tasks.pop(index)
                        print("Tache supprimée.")
                    else:
                        print("Numero invalide.")
            
            elif action == 'q':
                break

view = TaskView()
controller = TaskController(view)
controller.run()

