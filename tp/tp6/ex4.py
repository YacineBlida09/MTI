# File: python/tp/tp6/ex4.py
class Car:
    def __init__(self):
        self.seats = None
        self.transmission = None
        self.engine = None
    
    def __str__(self):
        return f"tonobil fiha {self.seats} krasa, boite {self.transmission}, moteur {self.engine}"


class CarBuilder:
    def __init__(self):
        self.car = Car()
    
    def set_seats(self, seats):
        self.car.seats = seats
        return self
    
    def set_transmission(self, transmission):
        self.car.transmission = transmission
        return self
    
    def set_engine(self, engine):
        self.car.engine = engine
        return self
    
    def build(self):
        return self.car


if __name__ == "__main__":

    maruti = (CarBuilder()
               .set_seats(4)
               .set_transmission("manuelle")
               .set_engine("0.5")
               .build())
    

    porche = (CarBuilder()
              .set_seats(2)
              .set_transmission("auto")
              .set_engine("v8")
              .build())
    
    custom = (CarBuilder()
              .set_seats(7)  
              .set_transmission("auto")  
              .set_engine("electrique")  
              .build())
    
    print("1. Maruti (Economy): ", maruti)
    print("2. Porche (Sports): ", porche)
    print("3. Custom : ", custom)
    
