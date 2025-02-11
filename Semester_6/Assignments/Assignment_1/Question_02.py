from decimal import Decimal as dec

class Account:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    @property
    def name(self):
        return self._name
    @property 
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= dec('0.00'):
            raise ValueError("Amount must be positive.\n")
        else:
            self._balance += amount
            print(f"Deposited {amount}$.\nUpdated balance: {self.balance}\n")

    def withdraw(self, amount):
        if amount <= dec('0.00'):
            raise ValueError("Amount must be positive.\n")
        elif amount > self._balance:
            raise ValueError("Insufficient Balance.\n")
        else:
            self._balance -= amount
            print(f"Withdrawn {amount}$.\nUpdated balance: {self.balance}\n")

    def __str__(self):
        return f"Account holder: {self.name}\nBalance: {self.balance}\n"


account = Account("Debadarshi Omkar", 10000)

print(account)

account.deposit(5000)
account.withdraw(2000)

print(account)