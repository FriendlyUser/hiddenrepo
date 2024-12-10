import psycopg2
from datetime import datetime
from typing import List, Dict

def aggregate_payments(interval: str = 'daily') -> List[Dict]:
    """
    Aggregate payment data based on specified time interval.
    
    Args:
        interval (str): Time interval for aggregation ('hour', 'day', or 'month')
    
    Returns:
        List[Dict]: List of dictionaries containing time buckets and average payment amounts
    """
    
    # Validate interval parameter
    valid_intervals = {'hour', 'day', 'month'}
    if interval.lower() not in valid_intervals:
        raise ValueError(f"Invalid interval. Must be one of: {', '.join(valid_intervals)}")
    
    # Define the date_trunc format based on interval
    date_trunc_format = interval.lower()
    
    try:
        # Database connection parameters
        db_params = {
            'host': 'postgres.c58u848ggx5b.us-west-1.rds.amazonaws.com',
            'database': 'pagila',
            'user': 'readonly_user',
            'password': 'labeling_now',
            'port': 5432
        }
        
        # Establish database connection
        conn = psycopg2.connect(**db_params)
        cursor = conn.cursor()
        
        # SQL query to aggregate payments
        query = """
            SELECT 
                DATE_TRUNC(%s, payment_date) as time_bucket,
                AVG(amount) as avg_amount,
                COUNT(*) as payment_count
            FROM payment
            GROUP BY time_bucket
            ORDER BY time_bucket;
        """
        
        # Execute query
        cursor.execute(query, (date_trunc_format,))
        
        # Fetch results and format them
        results = []
        for row in cursor.fetchall():
            time_bucket, avg_amount, payment_count = row
            results.append({
                'time_bucket': time_bucket.strftime('%Y-%m-%d %H:%M:%S'),
                'avg_amount': round(float(avg_amount), 2),
                'payment_count': payment_count
            })
        
        return results
    
    except psycopg2.Error as e:
        raise Exception(f"Database error: {str(e)}")
    
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()

# Example usage:
if __name__ == "__main__":
    try:
        # Get daily aggregation
        daily_results = aggregate_payments('hour')
        print("\nDaily Aggregation:")
        for result in daily_results[:5]:  # Print first 5 results
            print(result)
        
        # Get hourly aggregation
        hourly_results = aggregate_payments('day')
        print("\nHourly Aggregation:")
        for result in hourly_results[:5]:  # Print first 5 results
            print(result)
        
        # Get monthly aggregation
        monthly_results = aggregate_payments('month')
        print("\nMonthly Aggregation:")
        for result in monthly_results[:5]:  # Print first 5 results
            print(result)
            
    except Exception as e:
        print(f"Error: {str(e)}")