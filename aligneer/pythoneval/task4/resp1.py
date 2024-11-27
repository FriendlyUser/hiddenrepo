import logging
import time
from flask import Flask, jsonify, request
from psycopg2 import pool
from psycopg2.extras import RealDictCursor

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)

# Set up a connection pool
db_pool = pool.SimpleConnectionPool(
    1,  # Minimum number of connections
    10,  # Maximum number of connections
    host='postgres.c58u848ggx5b.us-west-1.rds.amazonaws.com',
    port=5432,
    user='readonly_user',
    password='labeling_now',
    database='pagila'
)

@app.route('/inventory-status', methods=['GET', 'POST'])
def inventory_status():
    start_time = time.time()
    connection = None
    cursor = None

    try:
        # Get a connection from the pool
        connection = db_pool.getconn()
        cursor = connection.cursor(cursor_factory=RealDictCursor)

        if request.method == 'POST':
            # Handle bulk queries
            inventory_ids = request.json.get('inventory_ids', [])
            if not inventory_ids:
                return jsonify({"error": "No inventory IDs provided"}), 400

            query = '''
                SELECT inventory_id, film_id, store_id, last_update
                FROM inventory
                WHERE inventory_id = ANY(%s)
            '''
            cursor.execute(query, (inventory_ids,))
        else:
            # Handle GET request
            query = '''
                SELECT inventory_id, film_id, store_id, last_update
                FROM inventory
            '''
            cursor.execute(query)

        inventory_data = cursor.fetchall()
        return jsonify(inventory_data)

    except Exception as e:
        logger.error(f"Error fetching inventory data: {e}")
        return jsonify({"error": "Internal server error"}), 500

    finally:
        # Close the cursor and return the connection to the pool
        if cursor:
            cursor.close()
        if connection:
            db_pool.putconn(connection)
        execution_time = time.time() - start_time
        logger.info(f"Request processed in {execution_time:.2f} seconds")

if __name__ == '__main__':
    app.run(debug=True)
