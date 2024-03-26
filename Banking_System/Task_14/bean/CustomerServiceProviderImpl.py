from datetime import datetime
from Account import  Account
from Task_14.Customer import Customer
from Account_type import SavingsAccount,CurrentAccount,ZeroBalanceAccount
from Task_14.Service.ICustomerServiceProvider import ICustomerServiceProvider
class CustomerServiceProviderImpl(ICustomerServiceProvider):
    def __init__(self):
        self.accounts = {}

    def create_account(self, customer, accNo, accType, balance):
        if accNo in self.accounts:
            print("Account number already exists!")
            return None

        if accType == "Savings":
            account = SavingsAccount(customer, 0.05, balance)
        elif accType == "Current":
            account = CurrentAccount(customer, 1000, balance)
        elif accType == "ZeroBalance":
            account = ZeroBalanceAccount(customer)
        else:
            print("Invalid account type!")
            return None

        self.accounts[accNo] = account
        return account

    def list_accounts(self):
        return list(self.accounts.values())

    def get_account_details(self, account_number):
        if account_number in self.accounts:
            account = self.accounts[account_number]
            customer = account.get_customer()
            return {"Account": account, "Customer": customer}
        else:
            print("Account not found!")
            return None

    def calculate_interest(self):
        for accNo, account in self.accounts.items():
            if isinstance(account, SavingsAccount):
                balance = account.get_account_balance()
                interest_rate = account.get_interest_rate()
                interest = balance * interest_rate
                print(f"Interest for account {accNo}: {interest}")


