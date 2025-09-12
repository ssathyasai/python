class Payment:
    def pay(self, amount):
        pass

class CashPayment(Payment):
    def pay(self, amount):
        print("Paid", amount, "in cash")

class CardPayment(Payment):
    def pay(self, amount):
        print("Paid", amount, "in Card")

class UPIpayment(Payment):
    def pay(self, amount):
        print("Paid", amount, "in UPI")


payments = [CashPayment(), CardPayment(), UPIpayment()]

for p in payments:
    p.pay(1000)   
