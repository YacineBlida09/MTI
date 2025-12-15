# File: python/tp/tp6/ex3.py
from abc import ABC, abstractmethod
from enum import Enum

# interface produit
class Chair(ABC):
    @abstractmethod
    def sit_on(self):
        pass
    
    @abstractmethod
    def get_style(self):
        pass

class Sofa(ABC):
    @abstractmethod
    def sleep_on(self):
        pass
    
    @abstractmethod
    def get_capacity(self):
        pass


class Table(ABC):
    @abstractmethod
    def put_on(self, item):
        pass
    
    @abstractmethod
    def get_size(self):
        pass


# concrete produits
class VictorianChair(Chair):
    def sit_on(self):
        return "9a3ed 3la korsi ml 3ahd el victori"
    
    def get_style(self):
        return "style victori"
    
    def __str__(self):
        return "korsi victori"


class VictorianSofa(Sofa):
    def sleep_on(self):
        return "ra9ed 3la sofa victoria"
    
    def get_capacity(self):
        return "trfd 3 3ibad"
    
    def __str__(self):
        return "sofa victoria"


class VictorianTable(Table):
    def put_on(self, kach_7aja):
        return f"n7atou {kach_7aja} 3la tabla victoria"
    
    def get_size(self):
        return "kbira"
    
    def __str__(self):
        return "table victoria"


class ModernChair(Chair):
    def sit_on(self):
        return "9a3ed 3la korsi modern"
    
    def get_style(self):
        return "style moderne"
    
    def __str__(self):
        return "korsi jdid"


class ModernSofa(Sofa):
    def sleep_on(self):
        return "ra9ed 3la sofa moderne"
    
    def get_capacity(self):
        return "trfd 6 3ibad"
    
    def __str__(self):
        return "sofa jdida"


class ModernTable(Table):
    def put_on(self, kach_7aja):
        return f"n7atou {kach_7aja} 3la tabla moderne"
    
    def get_size(self):
        return "sghira"
    
    def __str__(self):
        return "table jdida"


# Abstract Factory
class FurnitureFactory(ABC):
    @abstractmethod
    def create_chair(self) -> Chair:
        pass
    
    @abstractmethod
    def create_sofa(self) -> Sofa:
        pass
    
    @abstractmethod
    def create_table(self) -> Table:
        pass
    
    def create_furniture_set(self):
        chair = self.create_chair()
        sofa = self.create_sofa()
        table = self.create_table()
        return {"chair": chair, "sofa": sofa, "table": table}


# Concrete Factory 
class VictorianFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        return VictorianChair()
    
    def create_sofa(self) -> Sofa:
        return VictorianSofa()
    
    def create_table(self) -> Table:
        return VictorianTable()


class ModernFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        return ModernChair()
    
    def create_sofa(self) -> Sofa:
        return ModernSofa()
    
    def create_table(self) -> Table:
        return ModernTable()


# client
def client_code(factory: FurnitureFactory):

    print(f"\nn5dmou ensemble t3 {factory.__class__.__name__}")
    
    furniture_set = factory.create_furniture_set()
    
    chair = furniture_set["chair"]
    print(f"Chair: {chair}")
    print(f"  - {chair.sit_on()}")
    print(f"  - Style: {chair.get_style()}")
    
    sofa = furniture_set["sofa"]
    print(f"\nSofa: {sofa}")
    print(f"  - {sofa.sleep_on()}")
    print(f"  - Capacity: {sofa.get_capacity()}")
    
    table = furniture_set["table"]
    print(f"\nTable: {table}")
    print(f"  - {table.put_on('ktab')}")
    print(f"  - Size: {table.get_size()}")
    
    return furniture_set



class FuturisticChair(Chair):
    def sit_on(self):
        return "9a3ed 3la korsi ml merri5"
    
    def get_style(self):
        return "ml futur b ai"
    
    def __str__(self):
        return "Futuristic Chair"


class FuturisticSofa(Sofa):
    def sleep_on(self):
        return "sofa ml mosta9bal bl massage"
    
    def get_capacity(self):
        return "12 bnadem b chargeurs t3houm"
    
    def __str__(self):
        return "Futuristic  Sofa"


class FuturisticTable(Table):
    def put_on(self, kach_7aja):
        return f"7atina {kach_7aja} 3la table ml futur bla rejlin"
    
    def get_size(self):
        return "kima 7abit"
    
    def __str__(self):
        return "Futuristic Table"


class FuturisticFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        return FuturisticChair()
    
    def create_sofa(self) -> Sofa:
        return FuturisticSofa()
    
    def create_table(self) -> Table:
        return FuturisticTable()


if __name__ == "__main__":


    victorian_factory = VictorianFactory()
    victorian_set = client_code(victorian_factory)
    

    modern_factory = ModernFactory()
    modern_set = client_code(modern_factory)
    
    futuristic_factory = FuturisticFactory()
    futuristic_set = client_code(futuristic_factory)
    
