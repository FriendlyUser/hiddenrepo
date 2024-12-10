I am working on a self-healing component for our backend services. The goal is to detect when certain films in our database have not been rented for a long time and log them for further analysis. I have written a function called monitor_and_log_unrented_films that queries the database for films that haven't been rented in over a year and logs their details. Here's the code snippet:

import psycopg2
import logging
from datetime import datetime, timedelta

def monitor_and_log_unrented_films():
    try:
        conn = psycopg2.connect(
            host='postgres.c58u848ggx5b.us-west-1.rds.amazonaws.com',
            port=5432,
            user='readonly_user',
            password='your_password',
            database='pagila'
        )
        cursor = conn.cursor()
        one_year_ago = datetime.now() - timedelta(days=365)
        query = """
        SELECT film.film_id, film.title, MAX(rental.rental_date) as last_rented
        FROM film
        LEFT JOIN inventory ON film.film_id = inventory.film_id
        LEFT JOIN rental ON inventory.inventory_id = rental.inventory_id
        GROUP BY film.film_id
        HAVING MAX(rental.rental_date) IS NULL OR MAX(rental.rental_date) < %s;
        """
        cursor.execute(query, (one_year_ago,))
        unrented_films = cursor.fetchall()
        for film in unrented_films:
            logging.info(f"Film ID: {film[0]}, Title: {film[1]}, Last Rented: {film[2]}")
        cursor.close()
        conn.close()
    except Exception as e:
        logging.error(f"An error occurred: {e}")
I'm a bit worried that I might not be covering all the edge cases, especially with potential database connection issues or empty result sets. I'd like to create a comprehensive set of unit tests using pytest to ensure this function behaves correctly under various scenarios. This includes situations like:

The database connection failing.
The query execution throwing an exception.
Handling films that have never been rented.
Handling empty film tables or missing columns.
Ensuring the logging works correctly when films are found and when no films are found.
Could you help me write these unit tests? I want to make sure we've got as much coverage as possible to catch any potential issues in the monitoring logic.