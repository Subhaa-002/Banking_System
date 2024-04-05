from Task_11_12_13.Customer import Customer
class Account:
    account_number_generator = 1000

    def __init__(self, account_type: str, balance: float, customer: Customer):
        self.overdraft_limit = 1000
        self.account_number = Account.generate_account_number()
        self.account_type = account_type
        self.balance = balance
        self.customer = customer

    def get_account_number(self) -> int:
        return self.account_number

    def set_account_number(self, account_number: int):
        self.account_number = account_number

    def get_account_type(self) -> str:
        return self.account_type

    def set_account_type(self, account_type: str):
        self.account_type = account_type

    def get_balance(self) -> float:
        return self.balance

    def set_balance(self, balance: float):
        self.balance = balance

    def get_customer(self) -> Customer:
        return self.customer

    @classmethod
    def generate_account_number(cls):
        cls.account_number_generator += 1
        return cls.account_number_generator

    def set_customer(self, customer: Customer):
        self.customer = customer

    def __str__(self) -> str:
        return (f"Account Details:\nAccount Number: {self.account_number}\nAccount Type: {self.account_type}\nBalance: "
                f"{self.balance}\nCustomer Details:\n{self.customer}")
    def display_info(self):
        print("Account Details: ")
        print("Account Number:", self.account_number)
        print("Account Type:", self.account_type)
        print("Account Balance:", self.balance)