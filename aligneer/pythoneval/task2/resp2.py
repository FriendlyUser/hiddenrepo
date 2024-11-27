from flask import Flask, jsonify
import psycopg2
from psycopg2 import pool
import os
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Database connection details from environment variables
DB_HOST = os.getenv('DB_HOST', 'postgres.c58u848ggx5b.us-west-1.rds.amazonaws.com')
DB_USER = os.getenv('DB_USER', 'readonly_user')
DB_PORT = os.getenv('DB_PORT', '5432')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'labeling_now')  # Replace with actual password or use a secret manager
DB_NAME = os.getenv('DB_NAME', 'pagila')

# Initialize connection pool
try:
    connection_pool = psycopg2.pool.SimpleConnectionPool(
        1, 20,  # Min and max connections
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME
    )
    if connection_pool:
        logging.info("Connection pool created successfully")
except Exception as e:
    logging.error(f"Error creating connection pool: {e}")

@app.route('/data')
def get_data():
    conn = None
    try:
        # Get a connection from the pool
        conn = connection_pool.getconn()
        if conn:
            logging.info("Successfully received a connection from the pool")
            cur = conn.cursor()

            # Execute a SELECT query
            cur.execute('SELECT * FROM actor LIMIT 10;')
            rows = cur.fetchall()

            # Close the cursor and return the connection to the pool
            cur.close()
            connection_pool.putconn(conn)

            return jsonify(rows)
    except Exception as e:
        logging.error(f"Error fetching data: {e}")
        return jsonify({'error': str(e)})
    finally:
        # Ensure the connection is returned to the pool in case of an error
        if conn:
            connection_pool.putconn(conn)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
