from abc import ABC, abstractmethod
from typing import Optional

# Fine-grained, cohesive interfaces
class Workable(ABC):
    @abstractmethod
    def work(self) -> str:
        """Perform work tasks"""
        pass
    
    @abstractmethod
    def get_work_hours(self) -> float:
        """Get daily work hours"""
        pass

class Eatable(ABC):
    @abstractmethod
    def eat(self) -> str:
        """Consume food"""
        pass
    
    @abstractmethod
    def get_daily_calories(self) -> int:
        """Get required daily calories"""
        pass

class Sleepable(ABC):
    @abstractmethod
    def sleep(self) -> str:
        """Rest/sleep"""
        pass
    
    @abstractmethod
    def get_sleep_hours(self) -> float:
        """Get required sleep hours"""
        pass

class Payable(ABC):
    @abstractmethod
    def get_salary(self) -> float:
        """Get compensation"""
        pass
    
    @abstractmethod
    def get_payment_method(self) -> str:
        """Get payment method (bank, cash, etc.)"""
        pass

class Chargeable(ABC):
    @abstractmethod
    def charge(self) -> str:
        """Charge/recharge (for robots/machines)"""
        pass
    
    @abstractmethod
    def get_battery_level(self) -> float:
        """Get current battery level (0-100)"""
        pass

# Concrete implementations
class Human(Workable, Eatable, Sleepable, Payable):
    def __init__(self, name: str, job_title: str):
        self.name = name
        self.job_title = job_title
        self.energy_level = 100
    
    def work(self) -> str:
        self.energy_level -= 20
        return f"{self.name} is working as a {self.job_title}"
    
    def get_work_hours(self) -> float:
        return 8.0  # Standard work day
    
    def eat(self) -> str:
        self.energy_level = min(100, self.energy_level + 30)
        return f"{self.name} is eating lunch"
    
    def get_daily_calories(self) -> int:
        return 2500  # Average adult
    
    def sleep(self) -> str:
        self.energy_level = 100
        return f"{self.name} is sleeping"
    
    def get_sleep_hours(self) -> float:
        return 8.0  # Recommended sleep
    
    def get_salary(self) -> float:
        return 50000.0  # Annual salary
    
    def get_payment_method(self) -> str:
        return "Bank transfer"
    
    def get_energy_level(self) -> int:
        return self.energy_level

class Robot(Workable, Chargeable):
    def __init__(self, model: str, serial_number: str):
        self.model = model
        self.serial_number = serial_number
        self.battery_level = 100.0
    
    def work(self) -> str:
        if self.battery_level < 10:
            return f"{self.model} needs charging!"
        
        self.battery_level -= 15
        return f"{self.model} is performing automated tasks"
    
    def get_work_hours(self) -> float:
        return 24.0  # Robots can work continuously
    
    def charge(self) -> str:
        self.battery_level = 100.0
        return f"{self.model} is fully charged"
    
    def get_battery_level(self) -> float:
        return self.battery_level

class Intern(Human):  # Interns work but aren't paid (or paid less)
    def __init__(self, name: str):
        super().__init__(name, "Intern")
    
    def get_salary(self) -> float:
        return 0.0  # Unpaid internship
    
    def get_work_hours(self) -> float:
        return 4.0  # Part-time

class Consultant(Workable, Payable):
    """Consultant works and gets paid, but may not eat/sleep at workplace"""
    def __init__(self, name: str, hourly_rate: float):
        self.name = name
        self.hourly_rate = hourly_rate
    
    def work(self) -> str:
        return f"Consultant {self.name} is advising clients"
    
    def get_work_hours(self) -> float:
        return 6.0  # Flexible hours
    
    def get_salary(self) -> float:
        return self.hourly_rate * self.get_work_hours() * 20  # Approx monthly
    
    def get_payment_method(self) -> str:
        return "Invoice"

# Factory to create different worker types
class WorkerFactory:
    @staticmethod
    def create_human(name: str, job: str) -> Human:
        return Human(name, job)
    
    @staticmethod
    def create_robot(model: str) -> Robot:
        return Robot(model, f"SN{hash(model) % 10000:04d}")
    
    @staticmethod
    def create_intern(name: str) -> Intern:
        return Intern(name)
    
    @staticmethod
    def create_consultant(name: str, rate: float) -> Consultant:
        return Consultant(name, rate)

# Usage examples
def manage_workday(workables: list[Workable]):
    """Function that only cares about work capabilities"""
    print("=== Work Day Starting ===")
    for worker in workables:
        print(worker.work())
        print(f"Work hours: {worker.get_work_hours()}")
    print("=== Work Day Ended ===\n")

def process_payments(payables: list[Payable]):
    """Function that only cares about payment"""
    print("=== Processing Payments ===")
    for payable in payables:
        salary = payable.get_salary()
        method = payable.get_payment_method()
        print(f"Paying ${salary:,.2f} via {method}")
    print("=== Payments Completed ===\n")

def maintain_equipment(chargeables: list[Chargeable]):
    """Function that only cares about charging"""
    print("=== Equipment Maintenance ===")
    for equipment in chargeables:
        print(equipment.charge())
        print(f"Battery: {equipment.get_battery_level():.1f}%")
    print("=== Maintenance Completed ===\n")

# Create workers
factory = WorkerFactory()
workers = [
    factory.create_human("Alice", "Software Engineer"),
    factory.create_robot("RoboWorker-X1000"),
    factory.create_intern("Bob"),
    factory.create_consultant("Charlie", 150.0)
]

# Use appropriate interfaces
workables = [w for w in workers if isinstance(w, Workable)]
payables = [w for w in workers if isinstance(w, Payable)]
chargeables = [w for w in workers if isinstance(w, Chargeable)]

manage_workday(workables)
process_payments(payables)
maintain_equipment(chargeables)

# Check interface compliance
print("=== Interface Compliance Check ===")
for worker in workers:
    interfaces = []
    if isinstance(worker, Workable):
        interfaces.append("Workable")
    if isinstance(worker, Eatable):
        interfaces.append("Eatable")
    if isinstance(worker, Sleepable):
        interfaces.append("Sleepable")
    if isinstance(worker, Payable):
        interfaces.append("Payable")
    if isinstance(worker, Chargeable):
        interfaces.append("Chargeable")
    
    print(f"{type(worker).__name__}: {', '.join(interfaces)}")