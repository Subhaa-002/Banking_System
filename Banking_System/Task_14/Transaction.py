class Transaction:
    def __init__(self, account, description, date_time, transaction_type, transaction_amount):
        self.account = account
        self.description = description
        self.date_time = date_time
        self.transaction_type = transaction_type
        self.transaction_amount = transaction_amount

    # Getter methods
    def get_account(self):
        return self.account

    def get_description(self):
        return self.description

    def get_date_time(self):
        return self.date_time

    def get_transaction_type(self):
        return self.transaction_type

    def get_transaction_amount(self):
        return self.transaction_amount

    # Setter methods
    def set_account(self, account):
        self.account = account

    def set_description(self, description):
        self.description = description

    def set_date_time(self, date_time):
        self.date_time = date_time

    def set_transaction_type(self, transaction_type):
        self.transaction_type = transaction_type

    def set_transaction_amount(self, transaction_amount):
        self.transaction_amount = transaction_amount

    def print_info(self):
        print("Account:", self.account.get_account_number())
        print("Description:", self.description)
        print("Date and Time:", self.date_time)
        print("Transaction Type:", self.transaction_type)
        print("Transaction Amount:", self.transaction_amount)


