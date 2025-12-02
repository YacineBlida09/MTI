#1.​ Create an abstract class Vehicle with:
# ○​ abstract methods: start_engine(), stop_engine().
# 2.​ Create subclasses: Car, Bike, Truck implementing those methods differently.
# 3.​ Test: create a list of Vehicle references to Car, Bike, etc., and call their methods.
# 4.​ Bonus: Add a factory method to create vehicles dynamically by type.​
from abc import ABC, abstractmethod


class Vehicule(ABC):

    __engine: bool
    def __init__(self):
        self.engine = 0

    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

    def etat_engine(self):
        if self.engine != 0:
            print("marche")
        else:
            print("arret")

class Car(Vehicule):

    def __init__(self):
        super().__init__()
    
    def start_engine(self):
        self.engine = 1
        print(f"car est en marche {self.engine}")
    
    def stop_engine(self):
        self.engine = 0
        print(f"car est a l'arret {self.engine}")

class Bike(Vehicule):

    def __init__(self):
        super().__init__()

    def start_engine(self):
        self.engine = 1
        print(f"bike est en marche {self.engine}")

    def stop_engine(self):
        self.engine = 0
        print(f"bike est a l'arret {self.engine}")

class Truck(Vehicule):

    def __init__(self):
        super().__init__()

    def start_engine(self):
        self.engine = 1
        print(f"truck est en marche {self.engine}")

    def stop_engine(self):
        self.engine = 0
        print(f"truck est a l'arret {self.engine}")

vehicles = [Car(), Bike(), Truck()]

for vehicle in vehicles:
    vehicle.start_engine()
    vehicle.stop_engine()

def usine(vehicle_type):
    vehicle_type = str(vehicle_type).lower()
    if vehicle_type == "car":
        return Car()
    elif vehicle_type == "bike":
        return Bike()
    elif vehicle_type == "truck":
        return Truck()
    else:
        print("Type de véhicule inconnu")

vehicle = usine("car")
vehicle.start_engine()
vehicle.stop_engine()