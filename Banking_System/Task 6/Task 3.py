'''Task 3: Loop Structures
You are responsible for calculating compound interest on savings accounts for bank customers. You
need to calculate the future balance for each customer's savings account after a certain number of years.
Tasks:
1. Create a program that calculates the future balance of a savings account.
2. Use a loop structure (e.g., for loop) to calculate the balance for multiple customers.
3. Prompt the user to enter the initial balance, annual interest rate, and the number of years.
4. Calculate the future balance using the formula:
future_balance = initial_balance * (1 + annual_interest_rate/100)^years.
5. Display the future balance for each customer.'''

def calc_futureBalance(initial_balance,annual_interest_rate,years):
    return initial_balance * pow((1 + annual_interest_rate/100),years)

n=int(input("Enter number of customers... "))
for i in range(n):
    ib=int(input(f"Enter inital balance of Customer{i+1} : "))
    air=int(input("Enter annual interest rate : "))
    y=int(input("Enter total number of years :  "))
    print(f"The Future Balance : {calc_futureBalance(ib,air,y)}\n\n")
