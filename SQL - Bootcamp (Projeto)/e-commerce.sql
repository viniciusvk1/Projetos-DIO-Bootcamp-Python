CREATE DATABASE e_commerce;

USE e_commerce;

CREATE TABLE products (
  product_id INT NOT NULL AUTO_INCREMENT,
  product_name VARCHAR(255) NOT NULL,
  product_description VARCHAR(255) NOT NULL,
  product_price DECIMAL(10,2) NOT NULL,
  product_quantity INT NOT NULL,
  product_category VARCHAR(255) NOT NULL,
  PRIMARY KEY (product_id)
);

CREATE TABLE customers (
  customer_id INT NOT NULL AUTO_INCREMENT,
  customer_name VARCHAR(255) NOT NULL,
  customer_email VARCHAR(255) NOT NULL,
  customer_password VARCHAR(255) NOT NULL,
  customer_address VARCHAR(255) NOT NULL,
  customer_city VARCHAR(255) NOT NULL,
  customer_state VARCHAR(255) NOT NULL,
  customer_country VARCHAR(255) NOT NULL,
  customer_zip_code VARCHAR(255) NOT NULL,
  PRIMARY KEY (customer_id)
);

CREATE TABLE orders (
  order_id INT NOT NULL AUTO_INCREMENT,
  customer_id INT NOT NULL,
  order_date DATETIME NOT NULL,
  order_total DECIMAL(10,2) NOT NULL,
  order_status VARCHAR(255) NOT NULL,
  PRIMARY KEY (order_id)
);

CREATE TABLE order_items (
  order_item_id INT NOT NULL AUTO_INCREMENT,
  order_id INT NOT NULL,
  product_id INT NOT NULL,
  product_quantity INT NOT NULL,
  product_price DECIMAL(10,2) NOT NULL,
  product_total DECIMAL(10,2) NOT NULL,
  PRIMARY KEY (order_item_id)
);

ALTER TABLE orders ADD FOREIGN KEY (customer_id) REFERENCES customers (customer_id);

ALTER TABLE order_items ADD FOREIGN KEY (order_id) REFERENCES orders (order_id);

ALTER TABLE order_items ADD FOREIGN KEY (product_id) REFERENCES products (product_id);