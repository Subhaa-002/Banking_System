from Task_11_12_13.bean.Account import Account
class SavingsAccount(Account):
    def __init__(self, interest_rate, customer,balance):
        super().__init__(account_type='Savings', account_balance=balance,customer= customer)
        self.interest_rate = interest_rate

    def get_interest_rate(self):
        return self.interest_rate

    def set_interest_rate(self, interest_rate):
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest_amount = self.account_balance * (self.interest_rate / 100)
        self.account_balance += interest_amount
        print(f"Interest of ${interest_amount} added to the account balance.")



