

### Revised Prompt for Comprehensive Unit Test Coverage

I have written a Python function, `transform_data`, to process data records before loading them into a data warehouse. It formats fields like `date`, `amount`, and `currency`. The function works with the test data I have, but I want to ensure it handles all possible edge cases and unexpected inputs robustly.

Could you help me write comprehensive unit tests for this function using `pytest`? The tests should cover:

1. **Valid Inputs**: Ensure correct transformation for valid data.
2. **Malformed Inputs**:
   - Invalid date formats.
   - Non-numeric values for the `amount` field.
   - Missing or incorrect data types for `currency`.
3. **Missing Fields**: Check the function's behavior when one or more fields are missing.
4. **Additional Edge Cases**:
   - Empty dictionaries.
   - Extra fields in the input.
   - Completely invalid or empty values.

---

### Function to be tested

```python
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

```
