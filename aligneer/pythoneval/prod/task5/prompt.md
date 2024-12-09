Can you refactor this database querying script? It's a simple tool that retrieves customer information using Python's psycopg2 library, but it slows down a lot with larger ranges of customer IDs. Also, I haven't implemented any concurrency.

Here's the code:

import psycopg2

def get_customer_info(customer_id):
    conn = psycopg2.connect(
        host='postgres.c58u848ggx5b.us-west-1.rds.amazonaws.com',
        port=5432,
        user='readonly_user',
        password='your_password',
        database='pagila'
    )
    cur = conn.cursor()
    cur.execute("SELECT first_name, last_name, email FROM customer WHERE customer_id = %s", (customer_id,))
    result = cur.fetchone()
    conn.close()
    return result

def get_customers_info(start_id, end_id):
    customer_info_list = []
    for customer_id in range(start_id, end_id + 1):
        info = get_customer_info(customer_id)
        if info:
            customer_info_list.append(info)
    return customer_info_list

start = 1
end = 1000
customers = get_customers_info(start, end)
print("Customer information:", customers)
Could you refactor it to improve performance by adding threading or async?