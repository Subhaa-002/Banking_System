from datetime import datetime
from Task_14.bean.BankRepositoryImpl import BankRepositoryImpl
import pyodbc

class BankApp:
    def __init__(self):
        self.bank_repository = BankRepositoryImpl()

    def create_account(self):
        try:
            while True:
                print("\nCreate Account Menu:")
                print("1. Savings Account")
                print("2. Current Account")
                print("3. Zero Balance Account")

                choice = input("Enter choice (1/2/3): ")
                if choice == "1":
                    acc_type = "Savings"
                elif choice == "2":
                    acc_type = "Current"
                elif choice == "3":
                    acc_type = "ZeroBalance"
                else:
                    print("Invalid choice!")
                    continue

                customer_id = input("Enter customer ID: ")
                balance = float(input("Enter initial balance: "))
                acc_no = input("Enter account number: ")

                if self.bank_repository.create_account(customer_id, acc_no, acc_type, balance):
                    print("Account created successfully!")
                else:
                    print("Failed to create account!")

                choice = input("Do you want to create another account? (yes/no): ")
                if choice.lower() != "yes":
                    break
        except pyodbc.DatabaseError as e:
            print("Database error occurred:", e)

    def deposit(self):
        try:
            account_number = input("Enter account number: ")
            amount = float(input("Enter amount to deposit: "))
            if self.bank_repository.deposit(account_number, amount):
                print("Amount deposited successfully!")
            else:
                print("Failed to deposit amount!")
        except pyodbc.DatabaseError as e:
            print("Database error occurred:", e)

    def withdraw(self):
        try:
            account_number = input("Enter account number: ")
            amount = float(input("Enter amount to withdraw: "))
            if self.bank_repository.withdraw(account_number, amount):
                print("Amount withdrawn successfully!")
            else:
                print("Failed to withdraw amount!")
        except pyodbc.DatabaseError as e:
            print("Database error occurred:", e)


    def get_balance(self):
        account_number = input("Enter account number: ")
        balance = self.bank_repository.get_account_balance(account_number)
        if balance is not None:
            print("Current balance:", balance)
        else:
            print("Failed to get balance!")

    def transfer(self):
        from_account_number = input("Enter account number to transfer from: ")
        to_account_number = input("Enter account number to transfer to: ")
        amount = float(input("Enter amount to transfer: "))
        if self.bank_repository.transfer(from_account_number, to_account_number, amount):
            print("Amount transferred successfully!")
        else:
            print("Failed to transfer amount!")

    def get_account_details(self):
        account_number = input("Enter account number: ")
        details = self.bank_repository.get_account_details(account_number)
        if details:
            print("Account details:", details)
        else:
            print("Failed to get account details!")

    def list_accounts(self):
        accounts = self.bank_repository.list_accounts()
        if accounts:
            print("List of accounts:")
            for account in accounts:
                print(account)
        else:
            print("Failed to list accounts!")

    def get_transactions(self):
        account_number = input("Enter account number: ")
        from_date = input("Enter start date (YYYY-MM-DD): ")
        to_date = input("Enter end date (YYYY-MM-DD): ")
        from_date = datetime.strptime(from_date, "%Y-%m-%d")
        to_date = datetime.strptime(to_date, "%Y-%m-%d")
        transactions = self.bank_repository.get_transactions(account_number, from_date, to_date)
        if transactions:
            print("Transactions:")
            for transaction in transactions:
                print(transaction)
        else:
            print("Failed to get transactions!")

    def run(self):
        while True:
            print("\nBanking System Menu:")
            print("1. Create Account")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Get Balance")
            print("5. Transfer")
            print("6. Get Account Details")
            print("7. List Accounts")
            print("8. Get Transactions")
            print("9. Exit")

            choice = input("Enter your choice: ")
            try:
                if choice == "1":
                    self.create_account()
                elif choice == "2":
                    self.deposit()
                elif choice == "3":
                    self.withdraw()
                elif choice == "4":
                    self.get_balance()
                elif choice == "5":
                    self.transfer()
                elif choice == "6":
                    self.get_account_details()
                elif choice == "7":
                    self.list_accounts()
                elif choice == "8":
                    self.get_transactions()
                elif choice == "9":
                    print("Exiting...")
                    break
                else:
                    print("Invalid choice!")
            except Exception as e:
                print("An error occurred:", e)


if __name__ == "__main__":
    bank_app = BankApp()
    bank_app.run()
