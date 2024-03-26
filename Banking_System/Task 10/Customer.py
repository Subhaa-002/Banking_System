class Customer:
    def __init__(self, customer_id='', first_name='', last_name='', email='', phone_number='', address=''):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        if '@' in email and '.' in email:
            self.email = email
        else:
            print("Invalid email address.")
        if len(phone_number) == 10 and phone_number.isdigit():
            self.phone_number = phone_number
        else:
            print("Invalid phone number. Phone number must be 10 digits.")
        self.address = address

    def get_customer_id(self):
        return self.customer_id

    def set_customer_id(self, customer_id):
        self.customer_id = customer_id

    def get_first_name(self):
        return self.first_name

    def set_first_name(self, first_name):
        self.first_name = first_name

    def get_last_name(self):
        return self.last_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def get_email(self):
        return self.email

    def set_email(self, email):
        if '@' in email and '.' in email:
            self.email = email
        else:
            print("Invalid email address.")

    def get_phone_number(self):
        return self.phone_number

    def set_phone_number(self, phone_number):
        if len(phone_number) == 10 and phone_number.isdigit():
            self.phone_number = phone_number
        else:
            print("Invalid phone number. Phone number must be 10 digits.")

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

    def print_info(self):
        print("Customer ID:", self.customer_id)
        print("First Name:", self.first_name)
        print("Last Name:", self.last_name)
        print("Email Address:", self.email)
        print("Phone Number:", self.phone_number)
        print("Address:", self.address)






