class BankAccount:
    def __init__(self, account_number='', customer_name='', balance=0.0):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = balance

    def print_info(self):
        print("Account Number:", self.account_number)
        print("Customer Name:", self.customer_name)
        print("Balance:", self.balance)

    def deposit(self, amount):
        pass

    def withdraw(self, amount):
        pass

    def calculate_interest(self):
        pass


