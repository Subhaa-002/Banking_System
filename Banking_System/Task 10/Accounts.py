class Account:
    def __init__(self, account_number='', account_type='', account_balance=0.0, customer=None):
        #one of the attributes is an object of Customer class dont forget to pass that
        self.account_number = account_number
        self.account_type = account_type
        self.account_balance = account_balance
        self.customer = customer

    def get_account_number(self):
        return self.account_number

    def set_account_number(self, account_number):
        self.account_number = account_number

    def get_account_type(self):
        return self.account_type

    def set_account_type(self, account_type):
        self.account_type = account_type

    def get_account_balance(self):
        return self.account_balance

    def set_account_balance(self, account_balance):
        self.account_balance = account_balance

    def get_customer(self):
        return self.customer

    def set_customer(self, customer):
        self.customer = customer

    def print_info(self):
        print("Account Number:", self.account_number)
        print("Account Type:", self.account_type)
        print("Account Balance:", self.account_balance)
        print("Customer Information:")
        if self.customer:
            self.customer.print_info()


