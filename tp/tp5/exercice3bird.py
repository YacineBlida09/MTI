from abc import ABC, abstractmethod

class FauxBird(ABC):
    @abstractmethod
    def eat(self):
        pass
    
    @abstractmethod
    def fly(self):
        pass

class FauxEagle(FauxBird):
    def eat(self):
        print("aigle mange")
    
    def fly(self):
        print("aigle vole")

class FauxPenguin(FauxBird):  
    def eat(self):
        print("Penguin mange")
    
    def fly(self):
        print("Penguin essaie de voler mais ne peut pas")


class Bird(ABC):
    @abstractmethod
    def eat(self):
        pass
    
    @abstractmethod
    def move(self):
        pass

class FlyingBird(Bird):
    @abstractmethod
    def fly(self):
        pass
    
    def move(self):
        self.fly()

class SwimmingBird(Bird):
    @abstractmethod
    def swim(self):
        pass
    
    def move(self):
        self.swim()

class WalkingBird(Bird):
    @abstractmethod
    def walk(self):
        pass
    
    def move(self):
        self.walk()


class Eagle(FlyingBird):
    def eat(self):
        print("aigle mange")
    
    def fly(self):
        print("aigle vole")

class Penguin(SwimmingBird, WalkingBird):
    def eat(self):
        print("Penguin mange")
    
    def swim(self):
        print("Penguin nage")

    def walk(self):
        print("Penguin marche")

    def move(self):
        self.swim() 
        self.walk()


birds = [Penguin(), Eagle()]

for bird in birds:
    bird.eat()
    bird.move()