class BankAccount:
    def __init__(self):
        self.__balance = 0 

    def deposit(self, amount):
        self.__balance += amount
        print("Amount", amount, "added successfully")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(amount, "withdraw successful")
        else:
            print("Insufficient balance")

    def display_bal(self):
        print("The remaining balance:", self.__balance)

b1 = BankAccount()
b1.deposit(5000)
b1.withdraw(1000)
b1.display_bal()
