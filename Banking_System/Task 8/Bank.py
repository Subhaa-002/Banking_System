from Savings import Savings_Account
from Current import Current_Account
'''class Bank:
    def __init__(self):
        self.account = None

    def create_savings_account(self, account_number, initial_balance, interest_rate):
        self.account = Savings_Account(account_number, initial_balance, interest_rate)
        print("Savings Account created successfully.")

    def create_current_account(self, account_number, initial_balance, overdraft_limit):
        self.account = Current_Account(account_number, initial_balance, overdraft_limit)
        print("Current Account created successfully.")

    def deposit(self, amount):
        if self.account:
            self.account.deposit(amount)
        else:
            print("No account exists.")

    def withdraw(self, amount):
        if self.account:
            if isinstance(self.account, Savings_Account):
                self.account.withdraw(amount)
            elif isinstance(self.account, Current_Account):
                self.account.withdraw(amount)
            else:
                print("Invalid account type.")
        else:
            print("No account exists.")

    def calculate_interest(self):
        if self.account:
            if isinstance(self.account, Savings_Account):
                self.account.calculate_interest()
            else:
                print("Interest calculation is only applicable for savings accounts.")
        else:
            print("No account exists.")


def main():
    bank = Bank()
    while True:
        print("\n1. Create Savings Account")
        print("2. Create Current Account")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Calculate Interest")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            account_number = input("Enter account number: ")
            initial_balance = float(input("Enter initial balance: "))
            interest_rate = float(input("Enter interest rate: "))
            bank.create_savings_account(account_number, initial_balance, interest_rate)
        elif choice == '2':
            account_number = input("Enter account number: ")
            initial_balance = float(input("Enter initial balance: "))
            overdraft_limit = float(input("Enter overdraft limit: "))
            bank.create_current_account(account_number, initial_balance, overdraft_limit)
        elif choice == '3':
            amount = float(input("Enter amount to deposit: "))
            bank.deposit(amount)
        elif choice == '4':
            amount = float(input("Enter amount to withdraw: "))
            bank.withdraw(amount)
        elif choice == '5':
            bank.calculate_interest()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()'''

class Bank:
    a_no=int(input("Enter Account number: "))
    a_t=int(input("\nEnter Account type:\n1.Savings\n2.Current\n choice: "))
    a_b=float(input("\nEnter Account Balance: "))
    if a_t==1:
        interest=float(input("Enter Interest : "))
        account = Savings_Account(account_number=a_no, account_balance=a_b,interest_rate=interest)
        ch = int(input("\nMenu\n1.Deposit\n2.Withdraw\n3.Calculate Interest\nChoice: "))
    elif a_t==2:
        overdraft=int(input("Enter overdraft limit: "))
        account = Current_Account(account_number=a_no, account_balance=a_b,overdraft_limit=overdraft)
        ch = int(input("\nMenu\n1.Deposit\n2.Withdraw\nChoice: "))

    if ch==1:
        c=int(input("Deposit\n1.Float\n2.Int\n3.Double"))
        if c==1 or c==3:
            account.deposit(float(input("\nEnter amount to be deposited: ")))
        elif c==2:
            account.deposit(int(input("\nEnter amount to be deposited: ")))
    elif ch==2:
        c = int(input("Withdraw\n1.Float\n2.Int\n3.Double"))
        if c == 1 or c == 3:
            account.withdraw (float(input("\nEnter amount to be Withdrawn: ")))
        elif c == 2:
            account.withdraw(int(input("\nEnter amount to be Withdrawn: ")))
    elif ch==3:
        account.calculate_interest()
    else:
        print("Enter Valid Option!!!")

Bank()