import psycopg2
import logging
import time

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def get_stock(item_ids):
    """
    Retrieves the stock count for a list of item IDs from the database.

    Args:
        item_ids: A list of item IDs to retrieve stock counts for.

    Returns:
        A dictionary mapping item IDs to their corresponding stock counts.
    """

    start_time = time.time()
    logging.info("Starting stock retrieval for item IDs: %s", item_ids)

    try:
        conn = psycopg2.connect(
            host='postgres.c58u848ggx5b.us-west-1.rds.amazonaws.com',
            port=5432,
            database='pagila',
            user='readonly_user',
            password='labeling_now'
        )
        # Ensure consistent reads
        conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_REPEATABLE_READ)
        cursor = conn.cursor()

        # Use a parameterized query to prevent SQL injection
        if isinstance(item_ids, list):
            cursor.execute(
                "SELECT film_id, COUNT(*) FROM inventory WHERE film_id IN %s GROUP BY film_id",
                (tuple(item_ids),)
            )
        else:
            cursor.execute(
                "SELECT film_id, COUNT(*) FROM inventory WHERE film_id = %s GROUP BY film_id",
                (item_ids,)
            )

        results = dict(cursor.fetchall())
        conn.close()

        logging.info("Finished stock retrieval in %.2f seconds", time.time() - start_time)
        return results

    except Exception as e:
        logging.error("An error occurred while retrieving stock: %s", e)
        raise  # Re-raise the exception to be handled at a higher level if needed

# Example usage for single and bulk retrieval
print(get_stock(1))
print(get_stock([1, 2, 3]))
