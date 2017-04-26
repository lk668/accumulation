-- -----------------------------
-- Write by Damon Li
-- SQL语句不区分大小写
-- -----------------------------

-- Create Table

DROP TABLE IF EXISTS accounts;
CREATE TABLE accounts (
    account_id INT(10) NOT NULL AUTO_INCREMENT,
    customer_id INT(4) NOT NULL AUTO_INCREMENT,
    account_type ENUM('savings', 'credit') NOT NULL,
    balance FLOAT(9) NOT NULL DEFAULT '19',
    date_time DATE NOT NULL DEFAULT '2017-04-07',

    PRIMARY KEY (account_id),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) -- Create reference with customer_id in TABLE customers
) CHARSET=utf-8;

DROP TABLE IF EXISTS customers;
CREATE TABLE customers (
    customer_id INT(4) NOT NULL AUTO_INCREMENT,
    NAME VARCHAR(20) NOT NULL,
    ADDRESS VARCHAR(20) NOT NULL,
    CIRY VARCHAR(20) NOT NULL,
    
    PRIMARY KEY (customer_id),
) CHARSET=utf-8;

INSERT INTO customers VALUES ('1','damon','Beijing','Beijing');
INSERT INTO accounts VALUES ('1','1','savings','','2016-06-06');
