def extract_customer_entities(db_connection):
    """
    Retrieves customer data from the database and extracts entities.
    """
    try:
        cursor = db_connection.cursor()
        cursor.execute("SELECT customer_id, first_name, last_name, email FROM customer")
        customers = cursor.fetchall()
        entities = []
        for customer in customers:
            entity = {
                'customer_id': customer[0],
                'first_name': customer[1],
                'last_name': customer[2],
                'email': customer[3]
            }
            entities.append(entity)
        return entities
    except Exception as e:
        print(f"Error extracting customer entities: {e}")
        return []
