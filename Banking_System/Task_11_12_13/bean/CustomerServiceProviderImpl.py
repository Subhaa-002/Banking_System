from Task_11_12_13.Service.ICustomerServiceProvider import ICustomerServiceProvider
from Task_11_12_13.Exceptions.Exceptions import InvalidAccountException,InsufficientFundException


class CustomerServiceProviderImpl(ICustomerServiceProvider):
    def __init__(self):
        self.accounts = {}

    def get_account_balance(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number]["balance"]
        else:
            raise InvalidAccountException("Invalid account number.")

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number]["balance"] += amount
            return self.accounts[account_number]["balance"]
        else:
            raise InvalidAccountException("Invalid account number.")

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            if self.accounts[account_number]["balance"] >= amount:
                self.accounts[account_number]["balance"] -= amount
                return self.accounts[account_number]["balance"]
            else:
                raise InsufficientFundException("Insufficient funds for transfer.")

        else:
            raise InvalidAccountException("Invalid account number.")

    def transfer(self, from_account_number, to_account_number, amount):
        if from_account_number in self.accounts and to_account_number in self.accounts:
            if self.accounts[from_account_number]["balance"] >= amount:
                self.accounts[from_account_number]["balance"] -= amount
                self.accounts[to_account_number]["balance"] += amount
                print("Transfer successful.")
            else:
                raise InsufficientFundException("Insufficient funds for transfer.")
        else:
            raise InvalidAccountException("Invalid account number.")

    def get_account_details(self, account_number):
        if account_number in self.accounts:
            print("Account Details:")
            print("Account Number:", account_number)
            print("Account Type:", self.accounts[account_number]["type"])
            print("Account Balance:", self.accounts[account_number]["balance"])
            print("Customer Details:")
            self.accounts[account_number]["customer"].print_info()
        else:
            raise InvalidAccountException("Invalid account number.")

