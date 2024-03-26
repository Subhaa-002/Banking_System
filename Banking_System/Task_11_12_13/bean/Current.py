from Task_11_12_13.bean.Account import Account
from Task_11_12_13.Exceptions.Exceptions import OverDraftLimitExceededException

class CurrentAccount(Account):
    def __init__(self, overdraft_limit, balance,customer):
        super().__init__('Current', account_balance=balance, customer=customer)
        self.overdraft_limit = overdraft_limit

    def get_overdraft_limit(self):
        return self.overdraft_limit

    def set_overdraft_limit(self, overdraft_limit):
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.account_balance + self.overdraft_limit:
            self.account_balance -= amount
            print(f"Withdrawn ${amount}. New balance: ${self.account_balance}")
        else:
            raise OverDraftLimitExceededException("Amount exceeds Overdraft!!")



