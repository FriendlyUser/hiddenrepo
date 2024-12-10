Could you refactor the following Python code that interacts with a PostgreSQL database using psycopg2? The function process_transactions is riddled with nested logic, making it hard to read and maintain. I need it optimized for better readability and performance when processing large datasets. Please simplify the nested structures and improve the modularity by breaking it into smaller, reusable components.


```python
import psycopg2

def process_transactions(transactions):
    conn = psycopg2.connect(
        host='postgres.c58u848ggx5b.us-west-1.rds.amazonaws.com',
        database='pagila',
        user='readonly_user',
        password='dummy_password'  # Replace with actual password
    )
    cursor = conn.cursor()
    results = []
    for tx in transactions:
        if tx['type'] == 'customer_query':
            if 'customer_id' in tx:
                cursor.execute(
                    "SELECT first_name, last_name, email FROM customer WHERE customer_id = %s",
                    (tx['customer_id'],)
                )
                data = cursor.fetchone()
                if data:
                    results.append({
                        'customer_id': tx['customer_id'],
                        'first_name': data[0],
                        'last_name': data[1],
                        'email': data[2]
                    })
                else:
                    print('No customer found with ID:', tx['customer_id'])
            else:
                print('Customer ID missing in transaction')
        elif tx['type'] == 'film_query':
            if 'title' in tx:
                cursor.execute(
                    "SELECT film_id, description, release_year FROM film WHERE title = %s",
                    (tx['title'],)
                )
                data = cursor.fetchall()
                if data:
                    for film in data:
                        results.append({
                            'film_id': film[0],
                            'description': film[1],
                            'release_year': film[2]
                        })
                else:
                    print('No film found with title:', tx['title'])
            else:
                print('Film title missing in transaction')
        else:
            print('Unknown transaction type:', tx['type'])
    cursor.close()
    conn.close()
    return results
```