from datetime import datetime

def transform_data(record):
    """
    Transforms a data record by ensuring proper types and formats for fields.

    Args:
        record (dict): A dictionary containing keys 'date', 'amount', and 'currency'.

    Returns:
        dict or None: A transformed dictionary if successful, or None if any error occurs.
    """
    try:
        # Convert date string to datetime object
        record['date'] = datetime.strptime(record['date'], '%Y-%m-%d')
        
        # Ensure amount is a float
        record['amount'] = float(record['amount'])
        
        # Uppercase the currency code
        record['currency'] = record['currency'].upper()
        
        return record
    except (ValueError, KeyError):
        # Handle missing or malformed data
        return None