'''Task 5: Password Validation
Write a program that prompts the user to create a password for their bank account. Implement if
conditions to validate the password according to these rules:
• The password must be at least 8 characters long.
• It must contain at least one uppercase letter.
• It must contain at least one digit.
• Display appropriate messages to indicate whether their password is valid or not.'''

password=input("Enter your possible password : ")
if len(password)<8:
    print("The Password must be atleast 8 characters!!")
elif not any(char.isupper() for char in password):
    print("The Password must have atleast one uppercase letter!!")
elif not any(char.isdigit() for char in password):
    print("The Password must have atleast one digit!!")
else:
    print("The Password is valid!!")
