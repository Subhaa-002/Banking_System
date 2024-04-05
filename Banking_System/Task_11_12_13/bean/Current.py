from Task_11_12_13.bean.Account import (Account)
from Task_11_12_13.Customer import Customer
from Task_11_12_13.Exceptions.Exceptions import OverDraftLimitExceededException

class CurrentAccount(Account):
    def __init__(self, account_balance: float, customer: Customer, overdraft_limit: float):
        super().__init__("Current", account_balance, customer)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount: float):
        if self.balance + self.overdraft_limit < amount:
            raise OverDraftLimitExceededException("Overdraft limit exceeded")
        else:
            self.balance -= amount
            return f"Withdrawal successful. Updated balance: {self.balance}"