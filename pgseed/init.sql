-- Create customers table
CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    customer_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert customer data
INSERT INTO customers (customer_name, email)
VALUES 
('John Doe', 'johndoe@example.com'),
('Jane Smith', 'janesmith@example.com'),
('Bob Johnson', 'bobjohnson@example.com');

-- Create orders table
CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    order_date DATE NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    customer_id INT REFERENCES customers(customer_id)
);

-- Insert order data
INSERT INTO orders (order_date, amount, customer_id)
VALUES 
('2024-09-01', 100.50, 1),
('2024-09-02', 150.75, 2),
('2024-09-03', 200.00, 3);