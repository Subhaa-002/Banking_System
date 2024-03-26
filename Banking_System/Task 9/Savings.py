from Bank_Account import BankAccount
class SavingsAccount(BankAccount):
    def __init__(self, account_number='', customer_name='', balance=0.0, interest_rate=0.0):
        super().__init__(account_number, customer_name, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest_amount = self.balance * self.interest_rate / 100
        self.balance += interest_amount
        print(f"Interest of ${interest_amount} added to the account balance.")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"${amount} deposited successfully")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"${amount} withdrawn successfully")
            else:
                print("Insufficient balance")
        else:
            print("Invalid withdrawal amount")