from flask import Flask, request, jsonify
import asyncio
import logging
from logging.handlers import RotatingFileHandler
import numpy as np
from typing import List, Dict, Any
import psycopg2
from psycopg2.pool import SimpleConnectionPool
from functools import wraps
import json

# Configure logging
logging.basicConfig(
    handlers=[RotatingFileHandler('service.log', maxBytes=100000, backupCount=3)],
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s'
)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Database connection configuration
DB_CONFIG = {
    'host': 'postgres.c58u848ggx5b.us-west-1.rds.amazonaws.com',
    'user': 'readonly_user',
    'password': 'labeling_now',
    'port': 5432,
    'database': 'pagila'
}

# Create a connection pool
try:
    connection_pool = SimpleConnectionPool(
        minconn=1,
        maxconn=10,
        **DB_CONFIG
    )
    logger.info("Database connection pool created successfully")
except Exception as e:
    logger.error(f"Failed to create database connection pool: {str(e)}")
    raise


def validate_float_list(data: List[float]) -> bool:
    """Validate if all elements in the list are floating-point numbers."""
    return all(isinstance(x, (int, float)) for x in data)


def get_db_connection():
    """Get a database connection from the pool."""
    try:
        connection = connection_pool.getconn()
        return connection
    except Exception as e:
        logger.error(f"Error getting database connection: {str(e)}")
        raise


def return_db_connection(connection):
    """Return a connection to the pool."""
    connection_pool.putconn(connection)


async def process_data_async(data: List[float]) -> Dict[str, Any]:
    """
    Process the input data asynchronously.
    This is a placeholder for your actual data processing logic.
    """
    try:
        # Example processing: calculate basic statistics
        result = {
            'mean': float(np.mean(data)),
            'std': float(np.std(data)),
            'min': float(np.min(data)),
            'max': float(np.max(data))
        }
        return result
    except Exception as e:
        logger.error(f"Error processing data: {str(e)}")
        raise


def error_handler(f):
    """Decorator for handling errors in routes."""
    @wraps(f)
    def wrapper(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            logger.error(f"Error in route {f.__name__}: {str(e)}")
            return jsonify({
                'error': 'Internal server error',
                'message': str(e)
            }), 500
    return wrapper


@app.route('/process', methods=['POST'])
@error_handler
def process_data():
    """Handle POST requests with JSON payload containing float lists."""
    try:
        data = request.get_json()

        if not data or 'numbers' not in data:
            return jsonify({
                'error': 'Invalid input',
                'message': 'Request must include "numbers" field'
            }), 400

        numbers = data['numbers']

        if not isinstance(numbers, list) or not validate_float_list(numbers):
            return jsonify({
                'error': 'Invalid input',
                'message': 'Numbers must be a list of floating-point values'
            }), 400

        # Process data asynchronously
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        result = loop.run_until_complete(process_data_async(numbers))
        loop.close()

        # Query database example
        conn = get_db_connection()
        try:
            with conn.cursor() as cur:
                # Example query - modify according to your needs
                cur.execute("""
                    SELECT COUNT(*) 
                    FROM film 
                    WHERE rental_rate BETWEEN %s AND %s
                """, (min(numbers), max(numbers)))
                db_result = cur.fetchone()
                result['matching_films'] = db_result[0]
        finally:
            return_db_connection(conn)

        return jsonify({
            'status': 'success',
            'result': result
        }), 200

    except json.JSONDecodeError:
        return jsonify({
            'error': 'Invalid JSON',
            'message': 'Request body must be valid JSON'
        }), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
