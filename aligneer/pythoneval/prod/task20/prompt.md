
I am working on a Python backend project that retrieves data from a list of film IDs concurrently using the 'pagila' PostgreSQL database. I have a function that uses `concurrent.futures` to fetch film data, but it currently crashes the entire program if a database query fails. I need to:

1. Implement proper exception handling so that failures do not crash the program.
2. Add retry logic that will attempt up to three retries for each failed query.
3. Ensure that the final returned result matches the order of the input film IDs, even if some queries fail initially and must be retried.

Below is my current code. Please show me how to modify it to meet these requirements:

```python
import concurrent.futures
import psycopg2

def get_film_data(film_ids):
    def fetch_film(film_id):
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

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        results = executor.map(fetch_film, film_ids)
    return list(results)
```

Please provide an updated version of this code that adds proper error handling, retries up to three times for each failed query, and returns the data in the correct order without crashing.