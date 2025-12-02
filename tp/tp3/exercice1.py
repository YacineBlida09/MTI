#1.​ Create a Student class with attributes: name, age, grade.
# 2.​ Add methods: display_info() and is_passed().
# 3.​ Instantiate multiple students and display their details.
# 4.​ Bonus: Add a __str__() method for a nice print format.

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def display_info(self):
        print(f"nom: {self.name}, age: {self.age}, note: {self.grade}")
    
    def is_passed(self):
        if self.grade >= 10:
            print(f"{self.name} a passé")
        else:
            print(f"{self.name} a echoué")

    def __str__(self):
        return f"Student(nom={self.name}, age={self.age}, note={self.grade})"

student1 = Student("Yacine", 21, 15)
student2 = Student("Louay", 21, 19)

student1.display_info()
student2.display_info()

student1.is_passed()
student2.is_passed()

print(student1)
print(student2)