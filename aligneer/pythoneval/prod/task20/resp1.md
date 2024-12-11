To achieve the desired functionality, we need to implement exception handling, retry logic, and ensure that the results are returned in the correct order. Here's how you can modify your code to meet these requirements:

```python
import concurrent.futures
import psycopg2
from psycopg2 import OperationalError
import time

def get_film_data(film_ids):
    def fetch_film(film_id):
        retries = 3
        for attempt in range(retries):
            try:
                conn = psycopg2.connect(
                    host='postgres.c58u848ggx5b.us-west-1.rds.amazonaws.com',
                    database='pagila',
                    user='readonly_user',
                    password='dummy_password',
                    port=5432
                )
                with conn.cursor() as cur:
                    cur.execute('SELECT * FROM film WHERE film_id = %s', (film_id,))
                    result = cur.fetchone()
                conn.close()
                return result
            except OperationalError as e:
                print(f"Attempt {attempt + 1} failed for film_id {film_id}: {e}")
                time.sleep(1)  # Wait a bit before retrying
            except Exception as e:
                print(f"An error occurred for film_id {film_id}: {e}")
                break
        return None  # Return None if all retries fail

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        # Use a dictionary to map film_id to its future
        future_to_film_id = {executor.submit(fetch_film, film_id): film_id for film_id in film_ids}
        results = {}
        for future in concurrent.futures.as_completed(future_to_film_id):
            film_id = future_to_film_id[future]
            try:
                result = future.result()
                results[film_id] = result
            except Exception as e:
                print(f"An error occurred while processing film_id {film_id}: {e}")
                results[film_id] = None

    # Return results in the order of the input film_ids
    return [results[film_id] for film_id in film_ids]

# Example usage
film_ids = [1, 2, 3, 4, 5]
film_data = get_film_data(film_ids)
print(film_data)
```

### Key Changes:

1. **Exception Handling**: We catch `OperationalError` for database connection issues and a general `Exception` for any other errors. This prevents the program from crashing.

2. **Retry Logic**: We attempt to connect and fetch data up to three times for each film ID. If a query fails, we wait for a short period before retrying.

3. **Order Preservation**: We use a dictionary to map each `film_id` to its corresponding future. This allows us to collect results in the order of the input `film_ids`.

4. **Return None on Failure**: If all retries fail for a particular film ID, we return `None` for that ID, ensuring that the result list maintains the same length as the input list.