#1.​ Create a BankAccount class with private attributes: __balance, __owner.
# 2.​ Add methods:
# a.​ deposit(amount)
# b.​ withdraw(amount) (check sufficient balance)
# c.​ get_balance()
# 3.​ Test encapsulation: try accessing private variables directly and note behavior.
# 4.​ Bonus: add an account number auto-generator.

class BankAccount:
    __balance = None
    __owner = ""
    __numcompte = 1

    def __init__(self, balance, owner):
        self.__balance = balance
        self.__owner = owner
        self.__numcompte = BankAccount.__numcompte
        BankAccount.__numcompte += 1

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("depot impossi")
    
    def withdraw(self, amount):
        if amount > self.__balance:
            print("solde insuffisant")
        else:
            self.__balance -= amount

    def get_balance(self):
        print(f"balance = {self.__balance}")

    def get_numcompte(self):
        print(f"numcompte = {self.__numcompte}")

acc1 = BankAccount(12000, "Yacine")
acc1.get_balance()

acc1.deposit(3000)
acc1.get_balance()
acc1.withdraw(2000)
acc1.get_balance()
acc1.withdraw(20000)
acc1.get_balance()
acc1.get_numcompte()

acc2 = BankAccount(5000, "Louay")
acc2.get_numcompte()