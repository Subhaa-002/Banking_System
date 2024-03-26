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
