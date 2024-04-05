from Task_11_12_13.Customer import Customer
from Task_11_12_13.bean.BankServiceProviderImpl import BankServiceProviderImpl
from Task_11_12_13.bean.Account import Account
from Task_11_12_13.Exceptions import Exceptions
from Task_11_12_13.bean.Current import CurrentAccount
from Task_11_12_13.bean.Savings import SavingsAccount
from typing import List
from Task_11_12_13.bean.BankServiceProviderImpl import BankServiceProviderImpl


class BankApp:
    def __init__(self):
        self.accounts: List[Account] = []

    def run(self):
        print("------------------------------------------")
        while True:
            print("\nMenu:")
            print("1. Create Account")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Get Balance")
            print("5. Transfer")
            print("6. Get Account Details")
            print("7. List Accounts")
            print("8. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.create_account()
            elif choice == '2':
                self.deposit()
            elif choice == '3':
                self.withdraw()

            elif choice == '5':
                self.transfer()
            elif choice == '6':
                self.get_account_details()
            elif choice == '7':
                self.list_accounts()
            elif choice == '8':
                print("Exiting BankApp. Thank you!")
                break
            else:
                print("Invalid choice. Please try again.")

    def create_account(self):
        b=BankServiceProviderImpl()
        print("\nCreate Account:")
        customer_id = int(input("Enter Customer ID: "))
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        email = input("Enter Email Address: ")
        phone = input("Enter Phone Number: ")
        address = input("Enter Address: ")
        c = Customer(customer_id, first_name, last_name, email, phone, address)

        print("Select Account Type:")
        print("1. Savings Account")
        print("2. Current Account")
        print("3. Zero Balance Account")
        account_type_choice = input("Enter your choice: ")
        if account_type_choice == '1':
            account_type = 'Savings'
        elif account_type_choice == '2':
            account_type = 'Current'
        elif account_type_choice == '3':
            account_type = 'ZeroBalance'
        else:
            print("Invalid choice. Account creation failed.")
            return

        initial_balance = float(input("Enter Initial Balance: "))
        a = Account(account_type=account_type, customer=c, balance=initial_balance)
        acc_no = a.generate_account_number()

        account = self.b.create_account(customer=c, acc_no=acc_no, acc_type=account_type,
                                                            balance=initial_balance)
        if account is not None:
            print(f"Account created successfully! Account Number: {account.get_account_number()}")

    def list_accounts(self) -> List[Account]:
        return self.accounts

    def deposit(self, account_number: int, amount: float):
        if account_number is None:
            raise Exception("Account number cannot be None")

        account = self.find_account(account_number)
        if account is None:
            print("Account not found.")
        else:
            account.balance += amount
            print(f"Rs.{amount} deposited successfully!!")
            print(f"The New Balance is {account.balance}")

    def withdraw(self, account_number: int, amount: float):
        if account_number is None:
            raise Exception("Account number cannot be None")

        account = self.find_account(account_number)
        if account is None:
            print("Account not found.")
        elif not self.has_sufficient_funds(account_number, amount):
            raise Exception("Insufficient funds in the account")
        else:
            account.balance -= amount
            print(f"Rs.{amount} withdrawn successfully!!")
            print(f"The New Balance is {account.balance}")

    def transfer(self, from_account_number: int, to_account_number: int, amount: float):
        if from_account_number is None or to_account_number is None:
            raise Exception("Account numbers cannot be None")

        from_account = self.find_account(from_account_number)
        to_account = self.find_account(to_account_number)

        if from_account is None or to_account is None:
            print("One or both accounts not found.")
        elif not self.has_sufficient_funds(from_account_number, amount):
            raise Exception("Insufficient funds in the account")
        else:
            from_account.balance -= amount
            to_account.balance += amount
            print("Successful transfer")
    def get_account_details(self):
        b=BankServiceProviderImpl()
        account_number = int(input("Enter Account Number: "))
        Account.display_info(self.b.get_account_details(account_number))

    def withdraw_from_current_account(self, account_number: int, amount: float):
        if account_number is None:
            raise Exception("Account number cannot be None")

        account = self.find_account(account_number)
        if account is None:
            print("Account not found.")
        elif not self.is_overdraft_limit_exceeded(account_number, amount):
            raise Exception("Overdraft limit exceeded")

    def find_account(self, account_number: int):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None

    def has_sufficient_funds(self, account_number: int, amount: float):
        account = self.find_account(account_number)
        if account is None:
            return False
        return account.balance >= amount

    def is_overdraft_limit_exceeded(self, account_number: int, amount: float):
        account = self.find_account(account_number)
        if isinstance(account, CurrentAccount):
            max_withdrawal = account.balance + account.overdraft_limit
            return amount < max_withdrawal
        return False


def main():
    bank = BankApp()
    bank.run()




if __name__ == "__main__":
    main()