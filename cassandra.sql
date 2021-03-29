CREATE TABLE review_product_id (
    product_id text,
    review_id text,
    review_date date,
    review_title text,
    review_mark int
    PRIMARY KEY ((product_id), review_id)
);

CREATE TYPE review_customer_id(
    customer_id text,
    review_id text,
    review_date date,
    review_title text,
    review_mark int
    PRIMARY KEY ((customer_id), review_id)
);

CREATE TABLE review_product_id_star (
    product_id text,
    review_id text,
    review_date date,
    review_title text,
    review_mark int
    PRIMARY KEY ((product_id), review_id, review_mark)
);

CREATE TABLE all_products (
    review_id text,
    total_marks int,
    product_name text,
    product_category text
    PRIMARY KEY (review_id)
);

CREATE TABLE N_popular_products (
    review_id text,
    total_marks int,
    product_name text,
    product_category text
    PRIMARY KEY (review_id)
);

CREATE TABLE N_by_fraction_5 (
    review_id text,
    total_marks int,
    product_name text,
    product_category text
    PRIMARY KEY (review_id)
);

CREATE TABLE all_customers (
    review_id text,
    marketplace text,
    PRIMARY KEY (review_id)
);

CREATE TABLE haters (
    review_id text,
    marketplace text,
    PRIMARY KEY (review_id)
);

CREATE TABLE backers (
    review_id text,
    marketplace text,
    PRIMARY KEY (review_id)
);

CREATE TABLE N_most_productive (
    review_id text,
    marketplace text,
    PRIMARY KEY (review_id)
);
