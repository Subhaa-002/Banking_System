from CustomerServiceProviderImpl import CustomerServiceProviderImpl
from Task_14.Service.IBankServiceProvider import IBankServiceProvider
from Account_type import SavingsAccount,CurrentAccount,ZeroBalanceAccount
class BankServiceProviderImpl(CustomerServiceProviderImpl, IBankServiceProvider):
    def __init__(self, branch_name, branch_address):
        super().__init__()
        self.accountList = []
        self.transactionList = []
        self.branch_name = branch_name
        self.branch_address = branch_address

    def create_account(self, customer, accNo, accType, balance):
        account = super().create_account(customer, accNo, accType, balance)
        if account:
            self.accountList.append(account)
        return account

    def list_accounts(self):
        return self.accountList

    def get_account_details(self, account_number):
        for account in self.accountList:
            if account.get_account_number() == account_number:
                return {"Account": account, "Customer": account.get_customer()}
        print("Account not found!")
        return None

    def calculate_interest(self):
        for account in self.accountList:
            if isinstance(account, SavingsAccount):
                balance = account.get_account_balance()
                interest_rate = account.get_interest_rate()
                interest = balance * interest_rate
                print(f"Interest for account {account.get_account_number()}: {interest}")

    def create_transaction(self, transaction):
        self.transactionList.append(transaction)

    def list_transactions(self):
        return self.transactionList


