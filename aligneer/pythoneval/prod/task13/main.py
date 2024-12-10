import psycopg2
import logging
from datetime import datetime, timedelta

def monitor_and_log_unrented_films():
    try:
        conn = psycopg2.connect(
            host='postgres.c58u848ggx5b.us-west-1.rds.amazonaws.com',
            port=5432,
            user='readonly_user',
            password='labeling_now',
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