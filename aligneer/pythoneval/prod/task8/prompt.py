I'm developing a Flask application that interacts with a PostgreSQL database. I wrote a function that retrieves and displays customer information based on their first name and last name from the 'customer' table, but I want to ensure it's robust and handles all edge cases.

Here's the code:

```python
import psycopg2
from flask import Flask, jsonify

app = Flask(__name__)

def get_customer_by_name(first_name, last_name):
    try:
        connection = psycopg2.connect(
            host='postgres.c58u848ggx5b.us-west-1.rds.amazonaws.com',
            port='5432',
            database='pagila',
            user='readonly_user',
            password='dummy_password'  # Using dummy password
        )
        cursor = connection.cursor()
        query = """
        SELECT * FROM customer
        WHERE first_name = %s AND last_name = %s;
        """
        cursor.execute(query, (first_name, last_name))
        customers = cursor.fetchall()
        if customers:
            customer_list = []
            for customer in customers:
                customer_data = {
                    'customer_id': customer[0],
                    'store_id': customer[1],
                    'first_name': customer[2],
                    'last_name': customer[3],
                    'email': customer[4],
                    'address_id': customer[5],
                    'active': customer[6],
                    'create_date': customer[7],
                    'last_update': customer[8]
                }
                customer_list.append(customer_data)
            return jsonify(customer_list)
        else:
            return jsonify({'message': 'No customers found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
```

Could you help me write some unit tests for this function using pytest? I want to cover all possible edge cases including handling non-existent customer names, database connection errors, and when no data is returned.