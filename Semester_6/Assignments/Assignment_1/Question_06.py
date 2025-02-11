class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount:.2f}. Updated balance: ${self.__balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount:.2f}. Updated balance: ${self.__balance:.2f}")
        elif amount > self.__balance:
            print("Insufficient balance.")
        else:
            print("Withdraw amount must be positive.")

    def display_balance(self):
        print(f"Balance: ${self.balance:.2f}")


account = BankAccount("Debadarshi Omkar", 15000.0)
account.display_balance()
account.deposit(500)
account.withdraw(2000)
account.display_balance()


'''

Using private attributes in a class improves data security and prevents accidental modifications in the following ways:

-> Data Security: Private attributes ensure that critical data, like a bank account balance, is not directly accessible or modifiable from outside the class. This reduces the risk of unauthorized changes.

-> Controlled Access: Access to private attributes is restricted to specific methods, which allows the class to enforce rules (e.g., ensuring the balance doesn’t go negative).

-> Prevents Accidental Changes: Direct manipulation of private data is prevented, reducing the risk of errors or bugs due to invalid values being set.

-> Encapsulation: Private attributes are part of the principle of encapsulation, which hides the internal details of the class and exposes only necessary functionality, improving code maintainability.

-> Data Integrity: By controlling how data is accessed and modified, private attributes help ensure the integrity and consistency of the object's state.

'''