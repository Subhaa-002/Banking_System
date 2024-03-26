class ICustomerServiceProvider:
    def get_account_balance(self, account_number):
        pass

    def deposit(self, account_number, amount):
        pass

    def withdraw(self, account_number, amount):
        pass

    def transfer(self, from_account_number, to_account_number, amount):
        pass

    def get_account_details(self, account_number):
        pass
