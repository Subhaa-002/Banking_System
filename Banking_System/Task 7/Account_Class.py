class Account:
    def __init__(self, account_number='', account_type='', account_balance=0.0):
        self.__account_number = account_number
        self.__account_type = account_type
        self.__account_balance = account_balance

    def get_account_number(self):
        return self.__account_number

    def get_account_type(self):
        return self.__account_type

    def get_account_balance(self):
        return self.__account_balance

    def set_account_number(self, account_number):
        self.__account_number = account_number

    def set_account_type(self, account_type):
        self.__account_type = account_type

    def set_account_balance(self, account_balance):
        self.__account_balance = account_balance

    def print_info(self):
        print("Account Number:", self.__account_number)
        print("Account Type:", self.__account_type)
        print("Account Balance:", self.__account_balance)

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            print(f"${amount} deposited successfully.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0:
            if self.__account_balance >= amount:
                self.__account_balance -= amount
                print(f"${amount} withdrawn successfully.")
            else:
                print("Insufficient balance.")
        else:
            print("Invalid withdrawal amount.")

    def calculate_interest(self):
        interest_rate = 4.5 / 100
        interest_amount = self.__account_balance * interest_rate
        self.deposit(interest_amount)
        print(f"Interest of ${interest_amount} added to the account balance.")


