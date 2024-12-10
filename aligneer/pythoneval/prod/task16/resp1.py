import psycopg2
from psycopg2 import sql
from datetime import datetime

def aggregate_payments(interval):
    # Define the connection parameters
    conn_params = {
        'host': 'postgres.c58u848ggx5b.us-west-1.rds.amazonaws.com',
        'port': 5432,
        'dbname': 'pagila',
        'user': 'readonly_user',
        'password': 'labeling_now'  # Add the password here
    }
    
    # Validate the interval parameter
    if interval not in ['hourly', 'daily', 'monthly']:
        raise ValueError("Interval must be 'hourly', 'daily', or 'monthly'")
    
    # Define the time bucket format based on the interval
    time_bucket_format = {
        'hourly': 'YYYY-MM-DD HH24',
        'daily': 'YYYY-MM-DD',
        'monthly': 'YYYY-MM'
    }
    
    # Connect to the PostgreSQL database
    try:
        conn = psycopg2.connect(**conn_params)
        cursor = conn.cursor()
        
        # Construct the SQL query
        query = sql.SQL("""
            SELECT
                to_char(payment_date, {time_bucket}) AS time_bucket,
                AVG(amount) AS average_payment
            FROM
                payment
            GROUP BY
                time_bucket
            ORDER BY
                time_bucket
        """).format(time_bucket=sql.Literal(time_bucket_format[interval]))
        
        # Execute the query
        cursor.execute(query)
        
        # Fetch the results
        results = cursor.fetchall()
        
        # Transform the results into a list of dictionaries
        aggregated_payments = [
            {'time_bucket': row[0], 'average_payment': row[1]}
            for row in results
        ]
        
        # Close the cursor and connection
        cursor.close()
        conn.close()
        
        return aggregated_payments
    
    except Exception as e:
        print(f"An error occurred: {e}")
        if conn:
            conn.close()
        return []

# Example usage
print(aggregate_payments('daily'))