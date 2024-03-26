'''Task 6: Password Validation
Create a program that maintains a list of bank transactions (deposits and withdrawals) for a customer.
Use a while loop to allow the user to keep adding transactions until they choose to exit. Display the
transaction history upon exit using looping statements. '''

transaction_hist = []
curr = 0
while (1):
    print("1.Deposit\n2.Withdraw\n3.Exit\n")
    n = int(input("Enter Your Choice: "))
    if n == 1:
        amt = int(input("Enter the amount to Deposit: "))
        curr += amt
        print(curr)
        transaction_hist.append(["Deposit", amt])
        print(amt, " Successfully Deposited")
    elif n == 2:
        amt = int(input("Enter the amount to Withdrawl: "))
        print(curr)
        if amt <= curr:
            print(amt, " Successfully Withdrawn")
            curr -= amt
            transaction_hist.append(["Withdrawl", amt])
        else:
            print("Insufficient Balance")
    elif n == 3:
        for i in range(0, len(transaction_hist)):
            print(str(i + 1), ".", transaction_hist[i][0], ":", transaction_hist[i][1])
        break
    else:
        print("Invalid Choice")