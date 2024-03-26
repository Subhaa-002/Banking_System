'''Task 2: Nested Conditional Statements
Create a program that simulates an ATM transaction. Display options such as "Check Balance,"
"Withdraw," "Deposit,". Ask the user to enter their current balance and the amount they want to
withdraw or deposit. Implement checks to ensure that the withdrawal amount is not greater than the
available balance and that the withdrawal amount is in multiples of 100 or 500. Display appropriate
messages for success or failure.'''
def ATM_Transaction():
    ch=int(input("Enter your Choice \n1.Withdraw\n2.Deposit\n"))
    if ch==1:
        bal,amt=map(int,input("Enter your current balance and the amount to be withdrawn ").split())
        if bal>amt:
            if amt%100==0 or amt%500==0:
                print(f"Withdrawl successful\nCurrent Balance : {bal-amt}")
            else:
                print("Withdrawl amount must be multiple of 100 or 500")
        else:
            print("Insufficient Funds")

    elif ch==2:
        bal, amt = map(int, input("Enter your current balance and the amount to be Deposited ").split())
        if amt % 100 == 0 or amt % 500 == 0:
            print(f"Deposit successful\nCurrent Balance : {bal + amt}")
        else:
            print("Deposit amount must be multiple of 100 or 500")

ATM_Transaction()