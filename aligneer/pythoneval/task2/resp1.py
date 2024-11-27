from flask import Flask, jsonify
from typing import Dict, List, Any
import psycopg2
from psycopg2.pool import SimpleConnectionPool
from contextlib import contextmanager
import os
from functools import wraps
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Database configuration - Better to use environment variables
DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'postgres.c58u848ggx5b.us-west-1.rds.amazonaws.com'),
    'port': os.getenv('DB_PORT', '5432'),
    'user': os.getenv('DB_USER', 'readonly_user'),
    'password': os.getenv('DB_PASSWORD', 'labeling_now'),
    'database': os.getenv('DB_NAME', 'pagila')
}

# Create a connection pool
pool = SimpleConnectionPool(
    minconn=1,
    maxconn=10,
    **DB_CONFIG
)

@contextmanager
def get_db_connection():
    """Context manager for database connections."""
    conn = pool.getconn()
    try:
        yield conn
    finally:
        pool.putconn(conn)

def handle_errors(f):
    """Decorator to handle errors uniformly."""
    @wraps(f)
    def wrapper(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except psycopg2.Error as e:
            logger.error(f"Database error: {str(e)}")
            return jsonify({'error': 'Database error occurred'}), 500
        except Exception as e:
            logger.error(f"Unexpected error: {str(e)}")
            return jsonify({'error': 'Internal server error'}), 500
    return wrapper

@app.route('/data')
@handle_errors
def get_data() -> Dict[str, List[Any]]:
    """Fetch data from the database."""
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute('SELECT * FROM actor LIMIT 10;')
            columns = [desc[0] for desc in cur.description]
            rows = cur.fetchall()

            # Convert to list of dictionaries for better JSON serialization
            result = [dict(zip(columns, row)) for row in rows]

        return jsonify({'data': result})

@app.errorhandler(404)
def not_found(e):
    """Handle 404 errors."""
    return jsonify({'error': 'Resource not found'}), 404

@app.errorhandler(500)
def server_error(e):
    """Handle 500 errors."""
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
