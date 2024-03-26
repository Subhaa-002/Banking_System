from Task_11_12_13.Service import ICustomerServiceProvider
from Task_11_12_13.Exceptions.Exceptions import InsufficientFundException,InvalidAccountException
class CustomerServiceProviderImpl(ICustomerServiceProvider):
    def __init__(self):
        self.accounts = []

    def get_account_balance(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account.account_balance
        raise InvalidAccountException("Invalid account number.")

    def deposit(self, account_number, amount):
        for account in self.accounts:
            if account.account_number == account_number:
                account.account_balance += amount
                return account.account_balance
        raise InvalidAccountException("Invalid account number.")

    def withdraw(self, account_number, amount):
        for account in self.accounts:
            if account.account_number == account_number:
                if account.account_balance >= amount:
                    account.account_balance -= amount
                    return account.account_balance
                else:
                    raise InsufficientFundException("Insufficient funds.")
        raise InvalidAccountException("Invalid account number.")

    def transfer(self, from_account_number, to_account_number, amount):
        from_account = None
        to_account = None
        for account in self.accounts:
            if account.account_number == from_account_number:
                from_account = account
            elif account.account_number == to_account_number:
                to_account = account

        if from_account is None or to_account is None:
            raise InvalidAccountException("Invalid account number.")

        if from_account.account_balance >= amount:
            from_account.account_balance -= amount
            to_account.account_balance += amount
            print("Transfer successful.")
        else:
            raise InsufficientFundException("Insufficient funds for transfer.")
    def get_account_details(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                    print("Account Details:")
                    print("Account Number:", account.account_number)
                    print("Account Type:", account.account_type)
                    print("Account Balance:", account.account_balance)
                    print("Customer Details:")
                    account.customer.print_info()
                    return None
            raise InvalidAccountException("Invalid account number.")

