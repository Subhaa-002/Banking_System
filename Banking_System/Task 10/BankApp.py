from Bank import Bank
from Customer import Customer
class BankApp:
    def __init__(self):
        self.bank = Bank()

    def run(self):
        while True:
            print("\nBank Operations:")
            print("1. Create Account")
            print("2. Get Account Balance")
            print("3. Deposit")
            print("4. Withdraw")
            print("5. Transfer")
            print("6. Get Account Details")
            print("7. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.create_account()
            elif choice == '2':
                self.get_account_balance()
            elif choice == '3':
                self.deposit()
            elif choice == '4':
                self.withdraw()
            elif choice == '5':
                self.transfer()
            elif choice == '6':
                self.get_account_details()
            elif choice == '7':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

    def create_account(self):
        print("\nCreate Account:")
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        email = input("Enter email address: ")
        phone_number = input("Enter phone number: ")
        address = input("Enter address: ")
        customer = Customer(first_name=first_name, last_name=last_name, email=email, phone_number=phone_number, address=address)

        print("\nSelect Account Type:")
        print("1. Savings Account")
        print("2. Current Account")
        acc_type = input("Enter your choice: ")

        balance = float(input("Enter initial balance: "))
        account_number = self.bank.create_account(customer, "Savings" if acc_type == '1' else "Current", balance)
        print(f"Account created successfully. Account number: {account_number}")

    def get_account_balance(self):
        account_number = int(input("Enter account number: "))
        balance = self.bank.get_account_balance(account_number)
        if balance is not None:
            print(f"Account balance: {balance}")

    def deposit(self):
        account_number = int(input("Enter account number: "))
        amount = float(input("Enter deposit amount: "))
        balance = self.bank.deposit(account_number, amount)
        if balance is not None:
            print(f"Deposit successful. New balance: {balance}")

    def withdraw(self):
        account_number = int(input("Enter account number: "))
        amount = float(input("Enter withdrawal amount: "))
        balance = self.bank.withdraw(account_number, amount)
        if balance is not None:
            print(f"Withdrawal successful. New balance: {balance}")

    def transfer(self):
        from_account_number = int(input("Enter sender account number: "))
        to_account_number = int(input("Enter receiver account number: "))
        amount = float(input("Enter transfer amount: "))
        self.bank.transfer(from_account_number, to_account_number, amount)

    def get_account_details(self):
        account_number = int(input("Enter account number: "))
        self.bank.get_account_details(account_number)


if __name__ == "__main__":
    bank_app = BankApp()
    bank_app.run()
