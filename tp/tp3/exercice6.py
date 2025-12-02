#1.​ Create a Car class that has an Engine object (composition).
#2.​ Create a Driver class that drives a Car (aggregation).
#3.​ Show that destroying a car destroys the engine, but not the driver

class Engine:
    def __init__(self):
        print("Engine cree")

    def __del__(self):
        print("Engine detruit.")


class Car:
    def __init__(self):
        self.engine = Engine()
        print("Car cree")

    def __del__(self):
        print("Car detruite.")


class Driver:
    def __init__(self, name, car):
        self.name = name
        self.car = car
        print(f"Driver {self.name} créé")

    def __del__(self):
        print(f"Driver {self.name} detruit")


car = Car()
driver = Driver("Thor", car)

print("\ndetruire la voiture...")
del car  

print("\nmais le conducteur existe toujours:")
print(driver.name)

print("\ndetruire le conducteur...")
del driver