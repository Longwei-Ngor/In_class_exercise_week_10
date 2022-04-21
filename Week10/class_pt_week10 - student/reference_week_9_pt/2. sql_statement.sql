-- create tables, customer, product and sale

CREATE TABLE customer (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    `name` VARCHAR(255) NOT NULL,
    ph_number VARCHAR(255) NOT NULL,
    dob DATE
);

CREATE TABLE product (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    `name` VARCHAR(255) NOT NULL,
    description VARCHAR(255)
);

CREATE TABLE sale (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    created_on DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customer(id),
    FOREIGN KEY (product_id) REFERENCES product(id)
);

-- insert data to table

INSERT INTO customer (`name`, ph_number, dob) VALUES
    ("joe", "855998877", "2004-12-25"),
    ("jacky", "855993877", "2003-11-11"),
    ("janny", "855996877", "2002-10-02"),
    ("joey", "855798877", "2001-09-05"),
    ("smith", "855908877", "2000-08-01");


INSERT INTO product (`name`, description) VALUES
    ("pepsi", "soda"),
    ("coca-cola", "soda"),
    ("sandwich", "breakfast"),
    ("salad", "breakfast"),
    ("steak", "dinner");


INSERT INTO sale (customer_id, product_id) VALUES
    (2, 1),
    (3, 2),
    (4, 3),
    (1, 4),
    (2, 2),
    (4, 4);


-- select record base on criteria
-- get all customer record from the database
SELECT * from customer; 

-- select only name and ph number information from customer databsae where customer id eq 2
SELECT `name`, ph_number FROM customer where id = 2;


-- select data across table relationship
SELECT customer.id, customer.name as "customer name", customer.ph_number, customer.dob, product.name as "purchase item", sale.created_on as "purchase date"
FROM sale
INNER JOIN customer on customer.id = sale.customer_id
INNER JOIN product on product.id = sale.product_id  


-- update record 

UPDATE customer SET ph_number='855666612', dob = '01-01-2005' WHERE id = 1;

-- delete record 

DELETE FROM customer WHERE id = 4;