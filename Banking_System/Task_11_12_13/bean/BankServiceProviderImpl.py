from CustomerServiceProviderImpl import CustomerServiceProviderImpl
from Task_11_12_13.Service.IBankServiceProvider import IBankServiceProvider
from Task_11_12_13.bean.Savings import SavingsAccount
from Task_11_12_13.bean.Current import CurrentAccount
from Task_11_12_13.bean.ZeroBalance import ZeroBalanceAccount
class BankServiceProviderImpl(CustomerServiceProviderImpl, IBankServiceProvider):
    def __init__(self, branch_name, branch_address):
        super().__init__()
        self.account_list = []
        self.branch_name = branch_name
        self.branch_address = branch_address

    def create_account(self, customer, acc_no, acc_type, balance):
        if acc_type == 'Savings':
            rate=float(input("Enter Rate: "))
            account = SavingsAccount(interest_rate=rate, customer=customer,balance=balance )
        elif acc_type == 'Current':
            overdraft = float(input("Enter Overdraft limit: "))
            account = CurrentAccount(overdraft_limit=overdraft, balance=balance, customer=customer)
        elif acc_type == 'Zero_Balance':
            account = ZeroBalanceAccount(customer)

        self.account_list.append(account)
        return account


    def list_accounts(self):
        return self.account_list

    def calculate_interest(self):
        for account in self.account_list:
            if isinstance(account, SavingsAccount):
                account.calculate_interest()

    def get_branch_name(self):
        return self.branch_name

    def set_branch_name(self, branch_name):
        self.branch_name = branch_name

    def get_branch_address(self):
        return self.branch_address

    def set_branch_address(self, branch_address):
        self.branch_address = branch_address
