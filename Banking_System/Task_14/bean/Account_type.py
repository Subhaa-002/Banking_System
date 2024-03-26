from Task_14.Customer import Customer
from Account import Account
class SavingsAccount(Account):
    def __init__(self, customer, interest_rate, initial_balance):
        super().__init__("Savings", account_balance=initial_balance, customer=customer)
        self.interest_rate = interest_rate

    def get_interest_rate(self):
        return self.interest_rate

    def set_interest_rate(self, interest_rate):
        self.interest_rate = interest_rate


class CurrentAccount(Account):
    def __init__(self, customer, overdraft_limit, initial_balance):
        super().__init__("Current", account_balance=initial_balance, customer=customer)
        self.overdraft_limit = overdraft_limit

    def get_overdraft_limit(self):
        return self.overdraft_limit

    def set_overdraft_limit(self, overdraft_limit):
        self.overdraft_limit = overdraft_limit


class ZeroBalanceAccount(Account):
    def __init__(self, customer):
        super().__init__("Zero Balance", 0, customer)


# Example usage:
# Assuming we already have a Customer object 'customer1'
customer1 = Customer('123','a','b','s@.com',"1234567890",'123 Main St, City, Country')

# Create a SavingsAccount object
savings_account = SavingsAccount(customer1, 0.05)  # Interest rate of 5%

# Create a CurrentAccount object
current_account = CurrentAccount(customer1, 1000)  # Overdraft limit of 1000

# Create a ZeroBalanceAccount object
zero_balance_account = ZeroBalanceAccount(customer1)

# Print account information
print("Savings Account Information:")
savings_account.print_info()
print()

print("Current Account Information:")
current_account.print_info()
print()

print("Zero Balance Account Information:")
zero_balance_account.print_info()
