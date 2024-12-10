import psycopg2

def get_db_connection():
    return psycopg2.connect(
        host='postgres.c58u848ggx5b.us-west-1.rds.amazonaws.com',
        database='pagila',
        user='readonly_user',
        password='labeling_now'  # Replace with actual password
    )

def fetch_customer_data(cursor, customer_id):
    cursor.execute(
        "SELECT first_name, last_name, email FROM customer WHERE customer_id = %s",
        (customer_id,)
    )
    return cursor.fetchone()

def fetch_film_data(cursor, title):
    cursor.execute(
        "SELECT film_id, description, release_year FROM film WHERE title = %s",
        (title,)
    )
    return cursor.fetchall()

def process_customer_query(cursor, tx):
    if 'customer_id' not in tx:
        print('Customer ID missing in transaction')
        return None

    data = fetch_customer_data(cursor, tx['customer_id'])
    if data:
        return {
            'customer_id': tx['customer_id'],
            'first_name': data[0],
            'last_name': data[1],
            'email': data[2]
        }
    else:
        print('No customer found with ID:', tx['customer_id'])
        return None

def process_film_query(cursor, tx):
    if 'title' not in tx:
        print('Film title missing in transaction')
        return []

    data = fetch_film_data(cursor, tx['title'])
    if data:
        return [
            {
                'film_id': film[0],
                'description': film[1],
                'release_year': film[2]
            }
            for film in data
        ]
    else:
        print('No film found with title:', tx['title'])
        return []

def process_transactions(transactions):
    conn = get_db_connection()
    cursor = conn.cursor()
    results = []

    for tx in transactions:
        if tx['type'] == 'customer_query':
            result = process_customer_query(cursor, tx)
            if result:
                results.append(result)
        elif tx['type'] == 'film_query':
            results.extend(process_film_query(cursor, tx))
        else:
            print('Unknown transaction type:', tx['type'])

    cursor.close()
    conn.close()
    return results

transactions = [
    {'type': 'customer_query', 'customer_id': 1},
    {'type': 'film_query', 'title': 'Matrix'}
]

results = process_transactions(transactions)