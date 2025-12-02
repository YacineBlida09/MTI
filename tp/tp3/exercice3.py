#1.​ Create a Person class (name, age, speak()).
# 2.​ Create a Teacher and Student subclass:
# ​ Teacher: adds subject and teach().
#  Student: adds grade and study().
# 3.​ Show how both share the speak() method but override it differently.
# 4.​ Bonus: Use super() in constructors.​

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def speak(self):
        print(f"une personne: {self.name} est en train de parler")

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
    
    def speak(self):
        print(f"un prof: {self.name} est en train de parler")
    
    def teach(self):
        print(f"le prof {self.name} est en train d'expliquer")

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade
    
    def speak(self):
        print(f"un etudiant: {self.name} est en train de parler")
    
    def study(self):
        print(f"l'étudiant {self.name} est en train d'étudier")
    
p1 = Person("Thor", 200)
p1.speak()

t1 = Teacher("Odin", 1000, "Mythology")
t1.speak()
t1.teach()

s1 = Student("Loki", 350, "A")
s1.speak()
s1.study()