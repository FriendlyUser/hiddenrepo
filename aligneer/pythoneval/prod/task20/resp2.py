import concurrent.futures
import psycopg2
from psycopg2 import Error as PostgresError
import time
from typing import List, Optional, Any
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_db_connection():
    """Create and return a database connection."""
    return psycopg2.connect(
        host='postgres.c58u848ggx5b.us-west-1.rds.amazonaws.com',
        database='pagila',
        user='readonly_user',
        password='labeling_now',
        port=5432
    )

def fetch_film_with_retry(film_id: int, max_retries: int = 3) -> Optional[tuple]:
    """
    Fetch film data with retry logic.
    Returns the film data or None if all retries fail.
    """
    for attempt in range(max_retries):
        try:
            conn = create_db_connection()
            with conn.cursor() as cur:
                cur.execute('SELECT * FROM film WHERE film_id = %s', (film_id,))
                result = cur.fetchone()
                return result
        except PostgresError as e:
            logger.error(f"Attempt {attempt + 1} failed for film_id {film_id}: {str(e)}")
            if attempt < max_retries - 1:
                # Exponential backoff: 1s, 2s, 4s
                time.sleep(2 ** attempt)
                continue
            logger.error(f"All retries failed for film_id {film_id}")
            return None
        finally:
            try:
                conn.close()
            except (NameError, AttributeError):
                pass

def get_film_data(film_ids: List[int]) -> List[Optional[Any]]:
    """
    Fetch film data for multiple film IDs concurrently.
    Returns a list of results in the same order as input film_ids.
    Failed queries return None in the result list.
    """
    # Create a dictionary to store results with their original positions
    results_dict = {}
    
    def fetch_and_store(film_id: int, position: int) -> None:
        """Fetch film data and store it with its original position."""
        result = fetch_film_with_retry(film_id)
        results_dict[position] = result

    # Use ThreadPoolExecutor for concurrent execution
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        # Submit all tasks and store futures
        futures = [
            executor.submit(fetch_and_store, film_id, i)
            for i, film_id in enumerate(film_ids)
        ]
        
        # Wait for all futures to complete
        concurrent.futures.wait(futures)
        
        # Check for any exceptions in futures
        for future in futures:
            try:
                future.result()  # This will raise any exceptions that occurred
            except Exception as e:
                logger.error(f"Unexpected error in thread: {str(e)}")

    # Return results in original order
    return [results_dict.get(i) for i in range(len(film_ids))]

# Example usage
if __name__ == "__main__":
    # Example film IDs
    film_ids = [1, 2, 3, 4, 5]
    
    try:
        results = get_film_data(film_ids)
        
        # Process results
        for film_id, result in zip(film_ids, results):
            if result is None:
                print(f"Failed to fetch data for film_id: {film_id}")
            else:
                print(f"Successfully fetched data for film_id: {film_id}")
                
    except Exception as e:
        logger.error(f"Error in main execution: {str(e)}")