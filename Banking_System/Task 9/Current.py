from Bank_Account import BankAccount
class CurrentAccount(BankAccount):
    def __init__(self, account_number='', customer_name='', balance=0.0, overdraft_limit=0):
        super().__init__(account_number, customer_name, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if self.balance >= amount or (self.balance - amount) >= -self.overdraft_limit:
            self.balance -= amount
            print(f"${amount} withdrawn successfully.")
        else:
            print("Withdrawal amount exceeds overdraft limit.")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"${amount} deposited successfully")
        else:
            print("Invalid deposit amount")