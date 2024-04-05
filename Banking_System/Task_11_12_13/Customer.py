class Customer:
    def __init__(self, customer_id: int, first_name: str, last_name: str, email: str, phone: str, address: str):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.address = address

    def get_customer_id(self) -> int:
        return self.customer_id

    def set_customer_id(self, customer_id: int):
        self.customer_id = customer_id

    def get_first_name(self) -> str:
        return self.first_name

    def set_first_name(self, first_name: str):
        self.first_name = first_name

    def get_last_name(self) -> str:
        return self.last_name

    def set_last_name(self, last_name: str):
        self.last_name = last_name

    def get_email(self) -> str:
        return self.email

    def set_email(self, email: str):
        self.email = email

    def get_phone(self) -> str:
        return self.phone

    def set_phone(self, phone: str):
        self.phone = phone

    def get_address(self) -> str:
        return self.address

    def set_address(self, address: str):
        self.address = address

    def __str__(self) -> str:
        return (f"Customer ID: {self.customer_id}\nName: {self.first_name} {self.last_name}\nEmail: "
                f"{self.email}\nPhone: {self.phone}\nAddress: {self.address}")