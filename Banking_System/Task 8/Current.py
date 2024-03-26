from Account import Account
class Current_Account(Account):
    OVERDRAFT_LIMIT = 1000

    def __init__(self, account_number='', account_balance=0.0, overdraft_limit=0.0):
        super().__init__(account_number, 'Current', account_balance)
        self.__overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > 0:
            if self.get_account_balance() >= amount or (self.get_account_balance() - amount) >= -self.__overdraft_limit:
                self.set_account_balance(self.get_account_balance() - amount)
                print(f"${amount} withdrawn successfully")
            else:
                print("Withdrawal amount exceeds limits")
        else:
            print("Invalid withdrawal amount")