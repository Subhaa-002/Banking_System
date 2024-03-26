from Task_14.Customer import Customer
class Account:
    last_acc_no = 1000

    def __init__(self, account_type, account_balance, customer):
        self.account_number = Account.generate_account_number()
        self.account_type = account_type
        self.account_balance = account_balance
        self.customer = customer

    @staticmethod
    def generate_account_number():
        Account.last_acc_no += 1
        return Account.last_acc_no

    # Getter methods
    def get_account_number(self):
        return self.account_number

    def get_account_type(self):
        return self.account_type

    def get_account_balance(self):
        return self.account_balance

    def get_customer(self):
        return self.customer

    # Setter methods
    def set_account_type(self, account_type):
        self.account_type = account_type

    def set_account_balance(self, account_balance):
        self.account_balance = account_balance

    def set_customer(self, customer):
        self.customer = customer

    def print_info(self):
        print("Account Number:", self.account_number)
        print("Account Type:", self.account_type)
        print("Account Balance:", self.account_balance)
        print("Customer:", self.customer.get_first_name(), self.customer.get_last_name())


