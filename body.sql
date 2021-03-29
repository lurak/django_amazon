CREATE TABLE Review(
customer_id INTEGER,
product_id INTEGER,
review_id INTEGER,
review_data DATE,
review_star INTEGER,
review_title TEXT
);


CREATE TABLE Customer(
    customer_id INTEGER,
    marketplace TEXT
);


CREATE TABLE Product(
    product_id INTEGER,
    product_title TEXT,
    product_category TEXT,
    total_votes INTEGER
);

