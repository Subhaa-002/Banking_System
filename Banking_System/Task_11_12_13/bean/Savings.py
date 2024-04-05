from Task_11_12_13.bean.Account import Account
from Task_11_12_13.Customer import Customer
class SavingsAccount(Account):
    def __init__(self, account_balance: float, customer: Customer, interest_rate: float):
        super().__init__("Savings", account_balance, customer)
        self.interest_rate = interest_rate