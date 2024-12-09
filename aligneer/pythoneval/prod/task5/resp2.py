import psycopg2
from psycopg2 import pool
from concurrent.futures import ThreadPoolExecutor
from typing import List, Tuple
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class CustomerDatabase:
    def __init__(self, min_connections: int = 5, max_connections: int = 20):
        self.connection_pool = pool.ThreadedConnectionPool(
            minconn=min_connections,
            maxconn=max_connections,
            host='postgres.c58u848ggx5b.us-west-1.rds.amazonaws.com',
            port=5432,
            user='readonly_user',
            password='labeling_now',
            database='pagila'
        )

    def get_customer_info(self, customer_id: int) -> Tuple[str, str, str]:
        conn = self.connection_pool.getconn()
        try:
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT first_name, last_name, email FROM customer WHERE customer_id = %s",
                    (customer_id,)
                )
                return cur.fetchone()
        except Exception as e:
            logger.error(f"Error fetching customer {customer_id}: {e}")
            return None
        finally:
            self.connection_pool.putconn(conn)

    def get_customers_info_batch(self, customer_ids: List[int]) -> List[Tuple[str, str, str]]:
        conn = self.connection_pool.getconn()
        try:
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT first_name, last_name, email FROM customer WHERE customer_id = ANY(%s)",
                    (customer_ids,)
                )
                return cur.fetchall()
        except Exception as e:
            logger.error(f"Error fetching customers batch: {e}")
            return []
        finally:
            self.connection_pool.putconn(conn)

    def get_customers_info_parallel(self, start_id: int, end_id: int, batch_size: int = 100) -> List[Tuple[str, str, str]]:
        all_customer_info = []
        customer_ids = list(range(start_id, end_id + 1))
        
        # Split customer IDs into batches
        batches = [customer_ids[i:i + batch_size] for i in range(0, len(customer_ids), batch_size)]
        
        with ThreadPoolExecutor(max_workers=min(len(batches), 10)) as executor:
            results = list(executor.map(self.get_customers_info_batch, batches))
            
        # Flatten results
        for batch_result in results:
            all_customer_info.extend(batch_result)
            
        return all_customer_info

    def __del__(self):
        if hasattr(self, 'connection_pool'):
            self.connection_pool.closeall()

def main():
    start = 1
    end = 1000
    
    # Initialize database connection
    db = CustomerDatabase()
    
    # Get customer information using parallel processing
    logger.info("Fetching customer information...")
    customers = db.get_customers_info_parallel(start, end)
    logger.info(f"Retrieved {len(customers)} customers")
    
    # Print first few results as sample
    for customer in customers[:5]:
        logger.info(f"Customer: {customer}")

if __name__ == "__main__":
    main()