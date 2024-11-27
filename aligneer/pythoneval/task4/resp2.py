import psycopg2
from psycopg2.extras import DictCursor
from flask import Flask, jsonify, request
import logging
from contextlib import contextmanager
from functools import wraps
import time
from typing import List, Dict, Any
from psycopg2.pool import SimpleConnectionPool

app = Flask(__name__)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Database configuration
DB_CONFIG = {
    'host': 'postgres.c58u848ggx5b.us-west-1.rds.amazonaws.com',
    'port': 5432,
    'user': 'readonly_user',
    'password': 'labeling_now',
    'database': 'pagila'
}

# Connection pool configuration
pool = SimpleConnectionPool(
    minconn=1,
    maxconn=10,
    **DB_CONFIG
)

@contextmanager
def get_db_connection():
    """Context manager for database connections"""
    conn = pool.getconn()
    try:
        yield conn
    except Exception as e:
        logger.error(f"Database error: {str(e)}")
        raise
    finally:
        pool.putconn(conn)

def timer_decorator(f):
    """Decorator to measure execution time"""
    @wraps(f)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = f(*args, **kwargs)
        end_time = time.time()
        logger.info(f"{f.__name__} executed in {end_time - start_time:.2f} seconds")
        return result
    return wrapper

def get_inventory_items(cursor, film_ids: List[int] = None) -> List[Dict[str, Any]]:
    """Fetch inventory items with optional filtering by film_ids"""
    try:
        if film_ids:
            cursor.execute(
                """
                SELECT 
                    i.inventory_id,
                    i.film_id,
                    i.store_id,
                    i.last_update,
                    f.title as film_title
                FROM inventory i
                JOIN film f ON i.film_id = f.film_id
                WHERE i.film_id = ANY(%s)
                """,
                (film_ids,)
            )
        else:
            cursor.execute(
                """
                SELECT 
                    i.inventory_id,
                    i.film_id,
                    i.store_id,
                    i.last_update,
                    f.title as film_title
                FROM inventory i
                JOIN film f ON i.film_id = f.film_id
                """
            )

        columns = [desc[0] for desc in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return results
    except Exception as e:
        logger.error(f"Error fetching inventory: {str(e)}")
        raise

@app.route('/inventory-status')
@timer_decorator
def inventory_status():
    """Get inventory status with optional film_id filtering"""
    try:
        # Get film_ids from query parameters
        film_ids = request.args.getlist('film_id', type=int)

        with get_db_connection() as conn:
            with conn.cursor(cursor_factory=DictCursor) as cursor:
                results = get_inventory_items(cursor, film_ids if film_ids else None)

        return jsonify({
            'status': 'success',
            'count': len(results),
            'data': results
        })
    except Exception as e:
        logger.error(f"Error in inventory_status: {str(e)}")
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@app.route('/bulk-inventory', methods=['POST'])
@timer_decorator
def bulk_inventory():
    """Handle bulk inventory queries"""
    try:
        data = request.get_json()
        if not data or 'film_ids' not in data:
            return jsonify({
                'status': 'error',
                'message': 'Missing film_ids in request body'
            }), 400

        film_ids = data['film_ids']

        with get_db_connection() as conn:
            with conn.cursor(cursor_factory=DictCursor) as cursor:
                results = get_inventory_items(cursor, film_ids)

        return jsonify({
            'status': 'success',
            'count': len(results),
            'data': results
        })
    except Exception as e:
        logger.error(f"Error in bulk_inventory: {str(e)}")
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@app.teardown_appcontext
def shutdown_session(exception=None):
    """Clean up connection pool on app shutdown"""
    pool.closeall()

if __name__ == '__main__':
    app.run(debug=True)
