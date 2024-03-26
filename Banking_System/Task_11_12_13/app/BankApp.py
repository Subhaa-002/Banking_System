from Task_11_12_13.Customer import Customer
from Task_11_12_13.bean.BankServiceProviderImpl import BankServiceProviderImpl
from Task_11_12_13.bean.Account import Account


class BankApp:
    def __init__(self, bank_service_provider):
        self.bank_service_provider = bank_service_provider

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
            elif choice == '4':
                self.get_balance()
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
        print("\nCreate Account:")
        customer_id = input("Enter Customer ID: ")
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
        a=Account(account_type=account_type,customer=c,account_balance=initial_balance)
        acc_no=a.generate_account_number()

        account = self.bank_service_provider.create_account(customer=c,acc_no=acc_no,acc_type=account_type, balance=initial_balance)
        if account is not None:
            print(f"Account created successfully! Account Number: {account.get_account_number()}")

    def deposit(self):
        account_number = int(input("Enter Account Number: "))
        amount = float(input("Enter Deposit Amount: "))
        new_balance = self.bank_service_provider.deposit(account_number, amount)
        if new_balance is not None:
            print(f"Deposit successful! New balance: {new_balance}")

    def withdraw(self):
        account_number = int(input("Enter Account Number: "))
        amount = float(input("Enter Withdrawal Amount: "))
        new_balance = self.bank_service_provider.withdraw(account_number, amount)
        if new_balance is not None:
            print(f"Withdrawal successful! New balance: {new_balance}")

    def get_balance(self):
        account_number = int(input("Enter Account Number: "))
        balance = self.bank_service_provider.get_account_balance(account_number)
        if balance is not None:
            print(f"Current balance: {balance}")

    def transfer(self):
        from_account_number = int(input("Enter From Account Number: "))
        to_account_number = int(input("Enter To Account Number: "))
        amount = float(input("Enter Transfer Amount: "))
        self.bank_service_provider.transfer(from_account_number, to_account_number, amount)

    def get_account_details(self):
        account_number = int(input("Enter Account Number: "))
        self.bank_service_provider.get_account_details(account_number)

    def list_accounts(self):
        accounts = self.bank_service_provider.list_accounts()
        if accounts:
            print("\nList of Accounts:")
            for account in accounts:
                print(f"Account Number: {account.get_account_number()}, Account Type: {account.get_account_type()}, "
                      f"Balance: {account.get_account_balance()}")
        else:
            print("No accounts found.")


if __name__ == "__main__":
    bank_service_provider = BankServiceProviderImpl(branch_name=input("Enter Bank Branch name: "), branch_address=input("Enter Bank address: "))
    bank_app = BankApp(bank_service_provider)
    bank_app.run()