CREATE DATABASE IF NOT EXISTS sales_etl;

USE sales_etl;

CREATE TABLE IF NOT EXISTS sales_orders (
    OrderId INT PRIMARY KEY,
    Product VARCHAR(150) NOT NULL,
    Category VARCHAR(100) NOT NULL,
    SalesAmount DECIMAL(10, 2) NOT NULL,
    OrderDate DATE NOT NULL,
    Region VARCHAR(50) NOT NULL,
    CustomerName VARCHAR(150) NOT NULL
);