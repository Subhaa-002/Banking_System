from Account_Class import Account
class Bank:
    a_no=int(input("Enter Account number: "))
    a_t=input("\nEnter Account type: ")
    a_b=float(input("\nEnter Account Balance: "))
    account = Account(account_number=a_no,account_type=a_t,account_balance=a_b)
    ch=int(input("\nMenu\n1.Deposit\n2.Withdraw\n3.Calculate Interest\nChoice: "))
    if ch==1:
            account.deposit(float(input("\nEnter amount to be deposited: ")))
    elif ch==2:
            account.withdraw (float(input("\nEnter amount to be Withdrawn: ")))
    elif ch==3:
        account.calculate_interest()
    else:
        print("Enter Valid Option!!!")

Bank()
