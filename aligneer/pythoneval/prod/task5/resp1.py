import psycopg2
from psycopg2 import pool
from concurrent.futures import ThreadPoolExecutor, as_completed

# Create a connection pool
connection_pool = psycopg2.pool.SimpleConnectionPool(
    1,  # Minimum number of connections
    10, # Maximum number of connections
    host='postgres.c58u848ggx5b.us-west-1.rds.amazonaws.com',
    port=5432,
    user='readonly_user',
    password='labeling_now',
    database='pagila'
)

def get_customer_info(customer_id):
    conn = connection_pool.getconn()
    try:
        cur = conn.cursor()
        cur.execute("SELECT first_name, last_name, email FROM customer WHERE customer_id = %s", (customer_id,))
        result = cur.fetchone()
        cur.close()
        return result
    finally:
        connection_pool.putconn(conn)

def get_customers_info(start_id, end_id):
    customer_info_list = []
    with ThreadPoolExecutor(max_workers=10) as executor:
        future_to_customer_id = {executor.submit(get_customer_info, customer_id): customer_id for customer_id in range(start_id, end_id + 1)}
        for future in as_completed(future_to_customer_id):
            customer_id = future_to_customer_id[future]
            try:
                info = future.result()
                if info:
                    customer_info_list.append(info)
            except Exception as e:
                print(f"Error retrieving customer {customer_id}: {e}")
    return customer_info_list

start = 1
end = 1000
customers = get_customers_info(start, end)
print("Customer information:", customers)
