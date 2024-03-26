from Savings import SavingsAccount
from Current import CurrentAccount
class Bank:
    a_t = int(input("\nEnter Account type:\n1.Savings\n2.Current\n choice: "))
    a_no=int(input("Enter Account number: "))
    c_na = (input("Enter Customer Name: "))
    a_b=float(input("\nEnter Account Balance: "))
    if a_t==1:
        interest=float(input("Enter Interest : "))
        account = SavingsAccount(account_number=a_no,customer_name=c_na,balance=a_b ,interest_rate=interest)
        ch = int(input("\nMenu\n1.Deposit\n2.Withdraw\n3.Calculate Interest\nChoice: "))
    elif a_t==2:
        overdraft=int(input("Enter overdraft limit: "))
        account = CurrentAccount(account_number=a_no, customer_name=c_na,balance=a_b,overdraft_limit=overdraft)
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