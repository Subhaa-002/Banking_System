import pyodbc

class DBUtil:
    @staticmethod
    def getDBConn():
        connection = None
        try:
            connection = pyodbc.connect('Driver={SQL Server};'
                                        'Server=MS\SQLEXPRESS01;'
                                        'Database=HMBank;'
                                        'Trusted_Connection=yes;')
        except Exception as e:
            print("Connection failed:", e)
        return connection
