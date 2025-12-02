from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(PaymentMethod):
    def pay(self, amount):
        print(f"carte credit paiment: ${amount}")

class PayPalPayment(PaymentMethod):
    def pay(self, amount):
        print(f"paiment a travers paypal de: ${amount}")

class BitcoinPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Bitcoin paiment de: ${amount}")


class PaymentProcessor:
    def process_payment(self, amount, payment_method: PaymentMethod):
        payment_method.pay(amount)

processor = PaymentProcessor()
processor.process_payment(200, PayPalPayment())  