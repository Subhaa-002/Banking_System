'''Task 4: Looping, Array and Data Validation
You are tasked with creating a program that allows bank customers to check their account balances.
The program should handle multiple customer accounts, and the customer should be able to enter their
account number, balance to check the balance.
Tasks:
1. Create a Python program that simulates a bank with multiple customer accounts.
2. Use a loop (e.g., while loop) to repeatedly ask the user for their account number and
balance until they enter a valid account number.
3. Validate the account number entered by the user.
4. If the account number is valid, display the account balance. If not, ask the user to try again. '''

accounts = {
    1: 1000,
    2: 2000,
    3: 500,
}

def is_valid_account(acc_number):
    return acc_number in accounts

while True:
    ch=int(input("Enter choice\n1.Register your account\n2.Check your account"))
    if ch==2:
        acc_number = input("Enter your account number: ")
        if is_valid_account(acc_number):
            print(f"Your account balance is: ${accounts[acc_number]}")
            break
        else:
            print("Invalid account number. Please try again.")
    elif ch==1:
        acc_number = input("Enter your account number: ")
        bal =  input("Enter your balance: ")
        accounts[acc_number]=bal
        print("\nAccount Created!!")





