import psycopg2
from typing import List, Dict, Optional
from contextlib import contextmanager
from dataclasses import dataclass

# Configuration
DB_CONFIG = {
    'host': 'postgres.c58u848ggx5b.us-west-1.rds.amazonaws.com',
    'database': 'pagila',
    'user': 'readonly_user',
    'password': 'labeling_now'
}

# Data classes for type hints and structure
@dataclass
class CustomerData:
    customer_id: int
    first_name: str
    last_name: str
    email: str

@dataclass
class FilmData:
    film_id: int
    description: str
    release_year: int

class DatabaseError(Exception):
    """Custom exception for database-related errors"""
    pass

@contextmanager
def get_db_connection():
    """Context manager for database connections"""
    conn = None
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        yield conn
    except psycopg2.Error as e:
        raise DatabaseError(f"Database connection error: {str(e)}")
    finally:
        if conn:
            conn.close()

def fetch_customer_data(cursor, customer_id: int) -> Optional[CustomerData]:
    """Fetch customer data from database"""
    cursor.execute(
        """
        SELECT first_name, last_name, email 
        FROM customer 
        WHERE customer_id = %s
        """,
        (customer_id,)
    )
    data = cursor.fetchone()
    if data:
        return CustomerData(
            customer_id=customer_id,
            first_name=data[0],
            last_name=data[1],
            email=data[2]
        )
    return None

def fetch_film_data(cursor, title: str) -> List[FilmData]:
    """Fetch film data from database"""
    cursor.execute(
        """
        SELECT film_id, description, release_year 
        FROM film 
        WHERE title = %s
        """,
        (title,)
    )
    return [
        FilmData(
            film_id=row[0],
            description=row[1],
            release_year=row[2]
        )
        for row in cursor.fetchall()
    ]

def process_customer_transaction(cursor, transaction: Dict) -> Optional[Dict]:
    """Process customer-related transaction"""
    if 'customer_id' not in transaction:
        print('Customer ID missing in transaction')
        return None
    
    customer = fetch_customer_data(cursor, transaction['customer_id'])
    if not customer:
        print('No customer found with ID:', transaction['customer_id'])
        return None
    
    return customer.__dict__

def process_film_transaction(cursor, transaction: Dict) -> List[Dict]:
    """Process film-related transaction"""
    if 'title' not in transaction:
        print('Film title missing in transaction')
        return []
    
    films = fetch_film_data(cursor, transaction['title'])
    if not films:
        print('No film found with title:', transaction['title'])
        return []
    
    return [film.__dict__ for film in films]

def process_transactions(transactions: List[Dict]) -> List[Dict]:
    """Main function to process all transactions"""
    results = []
    
    try:
        with get_db_connection() as conn:
            with conn.cursor() as cursor:
                for tx in transactions:
                    transaction_type = tx.get('type')
                    
                    if transaction_type == 'customer_query':
                        result = process_customer_transaction(cursor, tx)
                        if result:
                            results.append(result)
                            
                    elif transaction_type == 'film_query':
                        results.extend(process_film_transaction(cursor, tx))
                        
                    else:
                        print('Unknown transaction type:', transaction_type)
                        
    except DatabaseError as e:
        print(f"Error processing transactions: {str(e)}")
        return []
        
    return results

transactions = [
    {'type': 'customer_query', 'customer_id': 1},
    {'type': 'film_query', 'title': 'Matrix'}
]

results = process_transactions(transactions)