from Task_14.Service.IBankRepository import IBankRepository
from Task_14.DBUtil import DBUtil
from Task_14.bean.Account_type import SavingsAccount,CurrentAccount,ZeroBalanceAccount
from Task_14.Transaction import Transaction
class BankRepositoryImpl(IBankRepository):
    def __init__(self):
        self.db_util = DBUtil()

    def create_account(self, customer, accNo, accType, balance):
        conn = self.db_util.getDBConn()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO Accounts (AccNo, AccType, Balance, CustomerID) VALUES (?, ?, ?, ?)",
                           (accNo, accType, balance, customer.get_customer_id()))
            conn.commit()
            return True
        except Exception as e:
            print("Error creating account:", e)
            conn.rollback()
            return False
        finally:
            cursor.close()
            conn.close()

    def list_accounts(self):
        accounts = []
        conn = self.db_util.getDBConn()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM Accounts")
            rows = cursor.fetchall()
            for row in rows:
                account_number, acc_type, balance, customer_id = row
                if acc_type == "Savings":
                    account = SavingsAccount(customer_id, 0.05, balance)
                elif acc_type == "Current":
                    account = CurrentAccount(customer_id, 1000, balance)
                elif acc_type == "ZeroBalance":
                    account = ZeroBalanceAccount(customer_id)
                accounts.append(account)
            return accounts
        except Exception as e:
            print("Error listing accounts:", e)
            return None
        finally:
            cursor.close()
            conn.close()

    def calculate_interest(self):
        conn = self.db_util.getDBConn()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM Accounts WHERE AccType='Savings'")
            rows = cursor.fetchall()
            for row in rows:
                account_number, acc_type, balance, customer_id = row
                account = SavingsAccount(customer_id, 0.05, balance)
                interest = account.get_account_balance() * account.get_interest_rate()
                print(f"Interest for account {account_number}: {interest}")
        except Exception as e:
            print("Error calculating interest:", e)
        finally:
            cursor.close()
            conn.close()

    def get_account_balance(self, account_number):
        conn = self.db_util.getDBConn()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT Balance FROM Accounts WHERE AccNo=?", (account_number,))
            row = cursor.fetchone()
            if row:
                return row[0]
            else:
                print("Account not found!")
                return None
        except Exception as e:
            print("Error getting account balance:", e)
            return None
        finally:
            cursor.close()
            conn.close()

    def deposit(self, account_number, amount):
        conn = self.db_util.getDBConn()
        cursor = conn.cursor()
        try:
            cursor.execute("UPDATE Accounts SET Balance = Balance + ? WHERE AccNo=?", (amount, account_number))
            conn.commit()
            return True
        except Exception as e:
            print("Error depositing amount:", e)
            conn.rollback()
            return False
        finally:
            cursor.close()
            conn.close()

    def withdraw(self, account_number, amount):
        conn = self.db_util.getDBConn()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT AccType, Balance FROM Accounts WHERE AccNo=?", (account_number,))
            row = cursor.fetchone()
            if row:
                acc_type, balance = row
                if acc_type == "Savings" and (balance - amount) < 500:
                    print("Withdrawal goes below minimum balance !")
                    return False
                elif acc_type == "Current" and (balance - amount) < -1000:
                    print("Withdrawal exceeds overdraft limit!")
                    return False
                else:
                    cursor.execute("UPDATE Accounts SET Balance = Balance - ? WHERE AccNo=?", (amount, account_number))
                    conn.commit()
                    return True
            else:
                print("Account not found!")
                return False
        except Exception as e:
            print("Error withdrawing amount:", e)
            conn.rollback()
            return False
        finally:
            cursor.close()
            conn.close()

    def transfer(self, from_account_number, to_account_number, amount):
        conn = self.db_util.getDBConn()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT Balance FROM Accounts WHERE AccNo=?", (from_account_number,))
            row = cursor.fetchone()
            if row:
                balance = row[0]
                if balance < amount:
                    print("Insufficient balance for transfer!")
                    return False
                else:
                    cursor.execute("UPDATE Accounts SET Balance = Balance - ? WHERE AccNo=?", (amount, from_account_number))
                    cursor.execute("UPDATE Accounts SET Balance = Balance + ? WHERE AccNo=?", (amount, to_account_number))
                    conn.commit()
                    return True
            else:
                print("Account not found!")
                return False
        except Exception as e:
            print("Error transferring amount:", e)
            conn.rollback()
            return False
        finally:
            cursor.close()
            conn.close()

    def get_account_details(self, account_number):
        conn = self.db_util.getDBConn()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM Accounts WHERE AccNo=?", (account_number,))
            row = cursor.fetchone()
            if row:
                account_number, acc_type, balance, customer_id = row
                customer = self.get_customer_details(customer_id)
                return {"Account": account_number, "Customer": customer}
            else:
                print("Account not found!")
                return None
        except Exception as e:
            print("Error getting account details:", e)
            return None
        finally:
            cursor.close()
            conn.close()

    def get_transactions(self, account_number, from_date, to_date):
        conn = self.db_util.getDBConn()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM Transactions WHERE AccountNumber=? AND Date >= ? AND Date <= ?",
                           (account_number, from_date, to_date))
            rows = cursor.fetchall()
            transactions = []
            for row in rows:
                description, date_time, transaction_type, transaction_amount = row
                transactions.append(
                    Transaction(account_number, description, date_time, transaction_type, transaction_amount))
            return transactions
        except Exception as e:
            print("Error getting transactions:", e)
            return None
        finally:
            cursor.close()
            conn.close()

