from Accounts import Account
from Customer import Customer
class Bank:
    def __init__(self):
        self.accounts = {}
        self.account_number_counter = 1000  # Starting account number

    def create_account(self, customer, acc_type, balance):
        self.account_number_counter += 1
        account_number = self.account_number_counter
        account = Account(account_number, acc_type, balance, customer)
        self.accounts[account_number] = account
        print(f"Account created successfully. Account number: {account_number}")
        return account_number

    def get_account_balance(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number].get_account_balance()
        else:
            print("Account not found.")
            return None

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number].deposit(amount)
            return self.accounts[account_number].get_account_balance()
        else:
            print("Account not found.")
            return None

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number].withdraw(amount)
            return self.accounts[account_number].get_account_balance()
        else:
            print("Account not found.")
            return None

    def transfer(self, from_account_number, to_account_number, amount):
        if from_account_number in self.accounts and to_account_number in self.accounts:
            if self.accounts[from_account_number].get_account_balance() >= amount:
                self.accounts[from_account_number].withdraw(amount)
                self.accounts[to_account_number].deposit(amount)
                print("Transfer successful.")
            else:
                print("Insufficient funds for transfer.")
        else:
            print("One or both accounts not found.")

    def get_account_details(self, account_number):
        if account_number in self.accounts:
            account = self.accounts[account_number]
            customer = account.get_customer()
            print("Account Details:")
            print("Account Number:", account_number)
            print("Account Type:", account.get_account_type())
            print("Account Balance:", account.get_account_balance())
            print("Customer Details:")
            if customer:
                customer.print_info()
        else:
            print("Account not found.")


