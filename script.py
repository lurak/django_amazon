import psycopg2
import pandas as pd
from datetime import datetime
import datetime

class DBInserter:
    def __init__(self, cursor, query):
        self.cursor = cursor
        self.query = query

    def insert_to_data_base(self, record_to_insert):
        self.cursor.execute(self.query, record_to_insert)


if __name__ == "__main__":
    path = "~/amazon_reviews_us_Books_v1_02.tsv"

    data = pd.read_csv(path, sep='\t', nrows=100)

    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="amazon")
        cursor = connection.cursor()
        product_inserter = DBInserter(cursor,
                                      f""" INSERT INTO review_product (product_id, product_title, product_category, total_votes) 
                                      VALUES (%s, %s, %s, %s)"""
                                      )
        reviews_inserter = DBInserter \
                (
                cursor,
                f""" INSERT INTO review_review 
            (customer_id, review_id, product_id, review_data, review_star, review_title) 
            VALUES (%s, %s, %s, %s, %s, %s)"""
            )

        customer_inserter = DBInserter \
                (
                cursor,
                f""" INSERT INTO review_customer 
                    (customer_id, marketplace ) 
                    VALUES (%s, %s)"""
            )
        customer_ids = list()
        product_ids = list()
        for i, row in data.iterrows():
            if row.product_id not in product_ids:
                records_to_insert_product = (row.product_id,
                                             row.product_title,
                                             row.product_category,
                                             row.total_votes)
                product_inserter.insert_to_data_base(records_to_insert_product)
                product_ids.append(row.product_id)
            # datetime.strptime(row.review_date[2:], "%y-%m-%d")
            records_to_insert_review = (row.customer_id,
                                        row.review_id,
                                        row.product_id,
                                        row.review_date,
                                        row.star_rating,
                                        row.review_headline)
            reviews_inserter.insert_to_data_base(records_to_insert_review)
            if row.customer_id not in customer_ids:
                records_to_insert_customer = (row.customer_id,
                                              row.marketplace)
                customer_inserter.insert_to_data_base(records_to_insert_customer)
                customer_ids.append(row.customer_id)
        connection.commit()
        print("OK")

    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into mobile table", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")