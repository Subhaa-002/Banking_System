#in python dictionary is the same as hashMap so this repeats the initial structure
from Task_11_12_13.Service import ICustomerServiceProvider
from Task_11_12_13.Exceptions.Exceptions import InsufficientFundException,InvalidAccountException
class CustomerServiceProviderImpl(ICustomerServiceProvider):
    def __init__(self):
        self.accounts = {}

    def get_account_balance(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            return account.account_balance
        else:
            raise InvalidAccountException("Invalid account number.")

    def deposit(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            account.account_balance += amount
            return account.account_balance
        else:
            raise InvalidAccountException("Invalid account number.")

    def withdraw(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            if account.account_balance >= amount:
                account.account_balance -= amount
                return account.account_balance
            else:
                raise InsufficientFundException("Insufficient funds.")
        else:
            raise InvalidAccountException("Invalid account number.")

    def transfer(self, from_account_number, to_account_number, amount):
        from_account = self.accounts.get(from_account_number)
        to_account = self.accounts.get(to_account_number)

        if from_account and to_account:
            if from_account.account_balance >= amount:
                from_account.account_balance -= amount
                to_account.account_balance += amount
                print("Transfer successful.")
            else:
                raise InsufficientFundException("Insufficient funds for transfer.")
        else:
            raise InvalidAccountException("Invalid account number.")

    def get_account_details(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            print("Account Details:")
            print("Account Number:", account.account_number)
            print("Account Type:", account.account_type)
            print("Account Balance:", account.account_balance)
            print("Customer Details:")
            account.customer.print_info()
        else:
            raise InvalidAccountException("Invalid account number.")
