/*Tasks 1: Database Design:   
1. Create the database named "HMBank"  
2. Define the schema for the Customers, Accounts, and Transactions tables based on the 
provided schema.  
4. Create an ERD (Entity Relationship Diagram) for the database.  
5. Create appropriate Primary Key and Foreign Key constraints for referential integrity.  
6. Write SQL scripts to create the mentioned tables with appropriate data types, constraints, 
and relationships.   
• Customers  
• Accounts 
• Transactions */
CREATE DATABASE HMBank;
USE HMBank;
CREATE TABLE Customers (
    customer_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    DOB DATE,
    email VARCHAR(100),
    phone_number VARCHAR(20),
    Address VARCHAR(255)
);

CREATE TABLE Accounts (
    account_id INT PRIMARY KEY,
    customer_id INT,
    account_type VARCHAR(50),
    balance INT,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);
CREATE TABLE Transactions (
    transaction_id INT PRIMARY KEY,
    account_id INT,
    transaction_type VARCHAR(50),
    amount INT,
    transaction_date DATE,
    FOREIGN KEY (account_id) REFERENCES Accounts(account_id)
);

			/*Tasks 2: Select, Where, Between, AND, LIKE:*/ 
/*1. Insert at least 10 sample records into each of the following tables.   
• Customers  
• Accounts 
• Transactions*/
INSERT INTO Customers (customer_id, first_name, last_name, DOB, email, phone_number, Address)
VALUES
(1, 'Rahul', 'Verma', '1988-03-15', 'rahul.verma@email.com', '9876543210', '123 MG Road,Mumbai'),
(2, 'Priya', 'Singh', '1992-06-25', 'priya.singh@email.com', '8765432109', '456 Park Street,Chennai'),
(3, 'Amit', 'Patel', '1985-11-10', 'amit.patel@email.com', '7654321098', '789 Market Lane,Delhi'),
(4, 'Neha', 'Sharma', '1990-09-18', 'neha.sharma@email.com', '6543210987', '101 Lotus Avenue,Mumbai'),
(5, 'Vikram', 'Gupta', '1982-02-08', 'vikram.gupta@email.com', '5432109876', '202 Tulip Street,Delhi'),
(6, 'Ananya', 'Joshi', '1995-04-30', 'ananya.joshi@email.com', '4321098765', '303 Rose Lane,Kochi'),
(7, 'Rajesh', 'Kumar', '1987-07-12', 'rajesh.kumar@email.com', '3210987654', '404 Lily Avenue,Trichy'),
(8, 'Sneha', 'Reddy', '1993-12-22', 'sneha.reddy@email.com', '2109876543', '505 Sunflower Street,Chennai'),
(9, 'Arun', 'Malhotra', '1980-05-05', 'arun.malhotra@email.com', '1098765432', '606 Jasmine Lane,Chennai'),
(10, 'Pooja', 'Rawat', '1998-08-20', 'pooja.rawat@email.com', '9876543210', '707 Orchid Avenue,Kochi');

INSERT INTO Accounts (account_id, customer_id, account_type, balance)
VALUES
(1, 1, 'savings',1000),
(2, 2, 'current',500),
(3, 3, 'savings',1500),
(4, 4, 'current',200),
(5, 5, 'savings',3000),
(6, 6, 'current',100),
(7, 7, 'zero_balance',0),
(8, 8, 'current',800),
(9, 9, 'zero_balance',0), 
(16, 2, 'current',1000),
(10, 10, 'current',1200);

INSERT INTO Transactions (transaction_id, account_id, transaction_type, amount, transaction_date)
VALUES
(1, 1, 'deposit', 500, '2024-03-01'),
(2, 2, 'withdrawal', 100, '2024-03-02'),
(3, 3, 'deposit', 200, '2024-03-03'),
(4, 4, 'withdrawal', 50, '2024-03-04'),
(5, 5, 'transfer', 300, '2024-03-05'),
(6, 6, 'deposit', 50, '2024-03-06'),
(7, 7, 'deposit', 20, '2024-03-07'),
(8, 8, 'transfer', 100, '2024-03-08'),
(9, 9, 'deposit', 150, '2024-03-09'),
(10, 10, 'withdrawal', 80, '2024-03-10'),
(11, 1, 'transfer', 200, '2024-03-11'),
(12, 2, 'deposit', 75, '2024-03-12'),
(13, 3, 'withdrawal', 30, '2024-03-13'),
(14, 4, 'deposit', 120, '2024-03-14'),
(15, 5, 'withdrawal', 50, '2024-03-15');

			/*2. Write SQL queries for the following tasks:*/

/*1. Write a SQL query to retrieve the name, account type and email of all customers. */
SELECT Customers.first_name,Customers.last_name,Customers.email,Accounts.account_type 
FROM Customers JOIN Accounts 
ON Accounts.customer_id=Customers.customer_id;

/*2.Write a SQL query to list all transaction corresponding customer. */
SELECT Transactions.* 
FROM Transactions JOIN Accounts 
ON Accounts.account_id=Transactions.account_id 
WHERE Accounts.customer_id=1;

/*3. Write a SQL query to increase the balance of a specific account by a certain amount. */
UPDATE Accounts
SET balance = balance + 10000 
WHERE account_id = 1;

/*4. Write a SQL query to Combine first and last names of customers as a full_name. */
SELECT customer_id,first_name + ' ' + last_name AS full_name
FROM Customers;

/*5. Write a SQL query to remove accounts with a balance of zero where the account  type is savings. */
DELETE FROM Accounts 
WHERE balance=0 AND account_type='Savings';

/*6. Write a SQL query to Find customers living in a specific city. */
SELECT * FROM Customers 
WHERE Address LIKE '%,Chennai';

/*7. Write a SQL query to Get the account balance for a specific account.*/
DECLARE @account_id INT =8;
SELECT balance FROM Accounts 
WHERE account_id=@account_id;

/*8. Write a SQL query to List all current accounts with a balance greater than $1,000. */
SELECT * FROM Accounts
WHERE account_type='Current' AND balance>1000;

/*9. Write a SQL query to Retrieve all transactions for a specific account. */
SELECT Transactions.* 
FROM Transactions JOIN Accounts 
ON Accounts.account_id=Transactions.account_id 
WHERE Accounts.account_id=1;

/*10. Write a SQL query to Calculate the interest accrued on savings accounts based on a given interest rate. */
DECLARE @INTREST INT = 5;
SELECT (balance *@INTREST*1)/100 AS Interest FROM Accounts
WHERE account_type='Savings';

/*11.Write a SQL query to Identify accounts where the balance is less than a specified overdraft limit. */
DECLARE @ODLIMIT INT = 500;
SELECT * FROM ACCOUNTS WHERE balance BETWEEN 0 AND @ODLIMIT;

/*12. Write a SQL query to Find customers not living in a specific city. */
SELECT * FROM Customers 
WHERE Address NOT LIKE '%,Chennai';


		/*Tasks 3: Aggregate functions, Having, Order By, GroupBy and Joins: */

/*1. Write a SQL query to Find the average account balance for all customers.   */
SELECT AVG(balance) AS AVG_BALANCE FROM Accounts;

/*2. Write a SQL query to Retrieve the top 10 highest account balances.  */
SELECT TOP 10 account_id,balance FROM Accounts 
ORDER BY balance DESC;

/*3. Write a SQL query to Calculate Total Deposits for All Customers in specific date. */
SELECT SUM(amount) as Total_DEPOSIT FROM Transactions 
WHERE transaction_date='2024-03-09' AND transaction_type='deposit';  

/*4. Write a SQL query to Find the Oldest and Newest Customers. */
SELECT MIN(account_id) AS Oldest, MAX(account_id) as Newest FROM Accounts;

/*5. Write a SQL query to Retrieve transaction details along with the account type. */
SELECT Transactions.*, Accounts.account_type FROM Transactions 
JOIN Accounts ON Transactions.account_id=Accounts.account_id;

/*6. Write a SQL query to Get a list of customers along with their account details. . */
SELECT Accounts.*, Customers.first_name,Customers.last_name FROM Accounts 
JOIN  Customers ON Customers.customer_id=Accounts.customer_id;

/*7. Write a SQL query to Retrieve transaction details along with customer information for a  specific account. */
SELECT Transactions.*,Customers.* FROM Transactions 
JOIN Accounts ON Transactions.account_id=Accounts.account_id 
JOIN Customers ON Customers.customer_id=Accounts.account_id;

/*8. Write a SQL query to Identify customers who have more than one account. */
SELECT Customers.customer_id,COUNT(Accounts.account_id) AS ACCOUNT_COUNT FROM Customers 
JOIN Accounts ON Customers.customer_id=Accounts.customer_id 
GROUP BY Customers.customer_id
HAVING COUNT(Accounts.account_id)>1;

/*9. Write a SQL query to Calculate the difference in transaction amounts between deposits and withdrawals. */
SELECT account_id,
SUM(CASE WHEN transaction_type = 'deposit' THEN amount ELSE 0 END) -
SUM(CASE WHEN transaction_type = 'withdrawal' THEN amount ELSE 0 END) AS difference
FROM Transactions
GROUP BY account_id;

/*10. Write a SQL query to Calculate the average daily balance for each account over a specified period.*/
SELECT AVG(Accounts.balance) as Average_balance FROM Accounts 
JOIN Transactions ON Accounts.account_id=Transactions.account_id 
WHERE Transactions.transaction_date BETWEEN '2024-03-01' AND '2024-03-09';

/*11. Calculate the total balance for each account type. */
SELECT  account_type,SUM(balance) as Total_balance FROM Accounts 
GROUP BY account_type;

/*12. Identify accounts with the highest number of transactions order by descending order.*/
SELECT account_id, COUNT(transaction_id) AS transaction_count
FROM Transactions
GROUP BY account_id
ORDER BY transaction_count DESC;

/*13. List customers with high aggregate account balances, along with their account types. */
SELECT Accounts.customer_id,Accounts.account_type,SUM(Accounts.balance) AS Aggregate_balance from Accounts  
GROUP BY Accounts.customer_id,Accounts.account_type 
ORDER BY SUM(Accounts.balance) DESC;

/*14. Identify and list duplicate transactions based on transaction amount, date, and account. */
SELECT DISTINCT account_id,amount,transaction_date,COUNT(transaction_id) AS Duplicate FROM Transactions 
GROUP BY amount,transaction_date,account_id 
HAVING COUNT(*)>1;

					/*Tasks 4: Subquery and its type: */

/*1. Retrieve the customer(s) with the highest account balance. */
SELECT customer_id,balance FROM Accounts 
WHERE balance IN 
(SELECT MAX(balance) FROM Accounts);

/*2. Calculate the average account balance for customers who have more than one account. */
SELECT customer_id, 
(SELECT AVG(balance) FROM Accounts WHERE customer_id = C.customer_id) AS average_balance
FROM Customers C
WHERE EXISTS
(SELECT * FROM Accounts A
WHERE A.customer_id = C.customer_id
GROUP BY A.customer_id
HAVING COUNT(A.account_id) > 1);

/*3. Retrieve accounts with transactions whose amounts exceed the average transaction amount. */
SELECT AVG(AMOUNT) AS AVERAGE FROM Transactions;
SELECT Accounts.*,Transactions.amount AS Transactions_account FROM Accounts 
JOIN Transactions ON Accounts.account_id=Transactions.account_id 
WHERE Transactions.amount>(SELECT AVG(amount) FROM Transactions);

/*4. Identify customers who have no recorded transactions. */
SELECT Customers.customer_id,Customers.first_name,Customers.last_name,Accounts.account_id FROM Customers 
JOIN Accounts ON Customers.customer_id=Accounts.account_id 
WHERE NOT EXISTS (SELECT * FROM Transactions WHERE Transactions.account_id=Accounts.account_id);

/*5. Calculate the total balance of accounts with no recorded transactions. */
SELECT Customers.customer_id,Customers.first_name,Customers.last_name,Accounts.account_id,(SELECT SUM(balance) FROM Accounts)AS TOTAL_BALANCE 
FROM Customers JOIN Accounts ON Customers.customer_id=Accounts.account_id 
WHERE NOT EXISTS (SELECT * FROM Transactions 
WHERE Transactions.account_id=Accounts.account_id);

/*6. Retrieve transactions for accounts with the lowest balance. */
SELECT MIN(balance) AS MIN_BALANCE FROM Accounts ;
SELECT Transactions.*,Accounts.balance FROM Transactions 
JOIN Accounts ON Transactions.account_id=Accounts.account_id 
WHERE Accounts.balance=(SELECT MIN(balance) FROM Accounts);

/*7. Identify customers who have accounts of multiple types. */
SELECT Customers.customer_id,Customers.first_name,Customers.first_name,Accounts.account_id 
FROM Customers JOIN Accounts 
ON Customers.customer_id=Accounts.account_id 
WHERE EXISTS 
(SELECT * FROM Accounts 
WHERE Accounts.customer_id = Customers.customer_id  
GROUP BY Accounts.customer_id 
HAVING COUNT(DISTINCT Accounts.account_type)>1);

/*8. Calculate the percentage of each account type out of the total number of accounts. */
SELECT Accounts.account_type, 100.0 * COUNT(*) / (SELECT COUNT(*) FROM Accounts) AS percentage
FROM Accounts 
GROUP BY Accounts.account_type;

/*9. Retrieve all transactions for a customer with a given customer_id. */
SELECT * FROM Transactions  
WHERE account_id IN (SELECT account_id FROM Accounts WHERE customer_id=2);

/*10. Calculate the total balance for each account type, including a subquery within the SELECT clause. */
SELECT account_type, (SELECT SUM(balance) FROM Accounts WHERE account_type = Accounts.account_type) AS total_balance
FROM Accounts 
GROUP BY account_type;