from Account import Account
class Savings_Account(Account):
    def __init__(self, account_number='', account_balance=0.0, interest_rate=0.0):
        super().__init__(account_number, 'Savings', account_balance)
        self.__interest_rate = interest_rate

    def calculate_interest(self):
        interest_amount = self.get_account_balance() * self.__interest_rate / 100
        self.deposit(interest_amount)
        print(f"Interest of ${interest_amount} added to the account balance")

