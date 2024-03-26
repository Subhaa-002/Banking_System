'''Task 1: Conditional Statements
Banking System
Control Structure
In a bank, you have been given the task is to create a program that checks if a customer is eligible for
a loan based on their credit score and income. The eligibility criteria are as follows:
• Credit Score must be above 700.
• Annual Income must be at least $50,000.
Tasks:
1. Write a program that takes the customer's credit score and annual income as input.
2. Use conditional statements (if-else) to determine if the customer is eligible for a loan.
3. Display an appropriate message based on eligibility. '''
def Eligibility_for_loan():
    credit_score,annual_income=map(int,input("Enter Credit Score and annual income... ").split())
    print('Eligible for loan' if (credit_score>700 and annual_income>50,000) else 'Not Eligible')
Eligibility_for_loan()