from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
import logging
import asyncio
import asyncpg

# Initialize Flask app
app = Flask(__name__)

# Configure database connection
app.config['SQLALCHEMY_DATABASE_URI'] = (
    'postgresql://readonly_user:labeling_now@postgres.c58u848ggx5b.us-west-1.rds.amazonaws.com:5432/pagila'
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Asynchronous function to query the database
async def query_database(query, params):
    conn = await asyncpg.connect(
        user='readonly_user',
        password='labeling_now',
        database='pagila',
        host='postgres.c58u848ggx5b.us-west-1.rds.amazonaws.com',
        port=5432
    )
    try:
        result = await conn.fetch(query, *params)
        return result
    finally:
        await conn.close()

# Function to validate input data
def check(data):
    if not isinstance(data, list):
        raise ValueError("Input data must be a list.")
    if not all(isinstance(x, float) for x in data):
        raise ValueError("All elements in the list must be floating-point numbers.")

# Asynchronous function to process data
async def process_data(data):
    # Example query based on input data
    query = "SELECT * FROM some_table WHERE some_column = ANY($1::float[])"
    result = await query_database(query, (data,))
    return result

# Route to handle POST requests
@app.route('/process', methods=['POST'])
async def handle_request():
    try:
        # Parse JSON payload
        data = request.json.get('numbers', [])
        
        # Validate input data
        check(data)
        
        # Process data asynchronously
        result = await process_data(data)
        
        # Return result as JSON
        return jsonify({'status': 'success', 'data': [dict(record) for record in result]})
    
    except ValueError as ve:
        logger.error(f"Validation error: {ve}")
        return jsonify({'status': 'error', 'message': str(ve)}), 400
    
    except SQLAlchemyError as se:
        logger.error(f"Database error: {se}")
        return jsonify({'status': 'error', 'message': 'Database error occurred.'}), 500
    
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return jsonify({'status': 'error', 'message': 'An unexpected error occurred.'}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
