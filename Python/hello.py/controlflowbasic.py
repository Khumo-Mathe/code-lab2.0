#system that processses different types of payments:crredit card, cryptoqurrency, and paypal

class PaymentMethod:
    def pay(self, amount):
        raise NotImplementedError("Subclasses should implement this!")
    
class CreditCard(PaymentMethod):
    def pay(self, amount):
        print(f"Paying {amount} using Credit Card")

class Cryptocurrency(PaymentMethod):
    def pay(self, amount):
        print(f"Paying {amount} using Cryptocurrency")

class PayPal(PaymentMethod):
    def pay(self, amount):
        print(f"Paying {amount} using PayPal")


class Order:
    def __init__(self, amount, payment_method: PaymentMethod):
        self.payment_method = payment_method

    def process_payment(self, amount):
        self.payment_method.pay(amount)