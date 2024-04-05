from Task_11_12_13.Service.IBankServiceProvider import IBankServiceProvider
from Task_11_12_13.bean.Account import Account
from Task_11_12_13.Customer import Customer
from Task_11_12_13.Exceptions.Exceptions import InsufficientFundException,InvalidAccountException,OverDraftLimitExceededException
from typing import Set,List
from Task_11_12_13.bean.Savings import SavingsAccount
from Task_11_12_13.bean.Current import CurrentAccount
class BankApp(IBankServiceProvider):
    def __init__(self):
        self.accounts: dict[int, Account] = {}

    def create_account(self, customer: Customer, accType: str, balance: float) -> int:
        new_account = None
        if accType is None:
            raise Exception("Account Type cannot be None")
        if accType == "Savings":
            new_account = SavingsAccount(balance, customer, 4.50)
        elif accType == "Current":
            new_account = CurrentAccount(balance, customer, 1000)

        self.accounts[new_account.account_number] = new_account
        # print(self.accounts)
        return new_account.account_number

    def list_accounts(self) -> List[Account]:
        return sorted(self.accounts.values(), key=lambda acc: acc.customer.first_name)

    def deposit(self, account_number: int, amount: float):
        if account_number is None:
            raise Exception("Account number cannot be None")
        if account_number in self.accounts:
            self.accounts[account_number].balance += amount
            print(f"Rs.{amount} deposited successfully!!")
            print(f"The New Balance is {self.accounts[account_number].balance}")

    def withdraw(self, account_number: int, amount: float):
        if not self.has_sufficient_funds(account_number, amount):
            raise InsufficientFundException("Insufficient funds in the account")
        else:
            self.accounts[account_number].balance -= amount
            print(f"Rs.{amount} withdrawn successfully!!")
            print(f"The New Balance is {self.accounts[account_number].balance}")

    def transfer(self, from_account_number: int, to_account_number: int, amount: float):
        if not self.is_valid_account(from_account_number) or not self.is_valid_account(to_account_number):
            raise InvalidAccountException("Invalid account number")

        if not self.has_sufficient_funds(from_account_number, amount):
            raise InsufficientFundException("Insufficient funds in the account")
        else:
            self.accounts[from_account_number].balance -= amount
            self.accounts[to_account_number].balance += amount
            print("Successful transfer")

    def withdraw_from_current_account(self, account_number: int, amount: float):
        if not self.is_overdraft_limit_exceeded(account_number, amount):
            raise OverDraftLimitExceededException("Overdraft limit exceeded")

    def has_sufficient_funds(self, account_number: int, amount: float):
        if account_number not in self.accounts:
            return False
        return self.accounts[account_number].balance >= amount

    def is_valid_account(self, account_number: int):
        return account_number in self.accounts

    def is_overdraft_limit_exceeded(self, account_number: int, amount: float):
        if account_number in self.accounts and isinstance(self.accounts[account_number], CurrentAccount):
            max_withdrawal = self.accounts[account_number].balance + self.accounts[account_number].overdraft_limit
            return amount < max_withdrawal
        return False


def main():
    bank = BankApp()

    try:
        c1 = Customer(1, "subha", "M", "subha@gmail.com", "1234567890", "ABC rd")
        a1 = BankApp.create_account(bank, c1, "Savings", 1000)

        c2 = Customer(2, "abc", "a", "abc@gmail.com", "1234567890", "ABC rd")
        a2 = BankApp.create_account(bank, c2, "Current", 2000)

        c3 = Customer(3, "xyz", "a", "xyz@gmail.com", "1234567890", "ABC rd")
        a2 = BankApp.create_account(bank, c3, "Current", 3000)

        print(bank.list_accounts())

        for account in bank.list_accounts():
            print(str(account))

        bank.deposit(1001, 1000)

    except Exception as e:
        print("Error:", e)

    # bank.deposit(1001, 1000)

    try:
        bank.withdraw(1001, 1000)
    except InsufficientFundException as e:
        print("Error:", e)

    try:
        bank.transfer(1001, 1002, 500)
    except InsufficientFundException as e:
        print("Error:", e)
    except InvalidAccountException as e:
        print("Error:", e)

    try:
        bank.withdraw_from_current_account(1002, 10)
    except OverDraftLimitExceededException as e:
        print("Error:", e)


if __name__ == "__main__":
    main()