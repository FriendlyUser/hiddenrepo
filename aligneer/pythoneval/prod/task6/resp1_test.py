import pytest
from unittest.mock import Mock, MagicMock
from db import extract_customer_entities  # Replace 'your_module' with the actual module name

def test_extract_customer_entities_normal_case():
    # Mock the database connection and cursor
    mock_db_connection = Mock()
    mock_cursor = Mock()
    mock_db_connection.cursor.return_value = mock_cursor
    
    # Define the expected data returned by the cursor
    mock_cursor.fetchall.return_value = [
        (1, 'John', 'Doe', 'john.doe@example.com'),
        (2, 'Jane', 'Smith', 'jane.smith@example.com')
    ]
    
    # Call the function
    result = extract_customer_entities(mock_db_connection)
    
    # Define the expected result
    expected_result = [
        {'customer_id': 1, 'first_name': 'John', 'last_name': 'Doe', 'email': 'john.doe@example.com'},
        {'customer_id': 2, 'first_name': 'Jane', 'last_name': 'Smith', 'email': 'jane.smith@example.com'}
    ]
    
    # Assert the result matches the expected result
    assert result == expected_result

def test_extract_customer_entities_empty_result():
    # Mock the database connection and cursor
    mock_db_connection = Mock()
    mock_cursor = Mock()
    mock_db_connection.cursor.return_value = mock_cursor
    
    # Define the empty data returned by the cursor
    mock_cursor.fetchall.return_value = []
    
    # Call the function
    result = extract_customer_entities(mock_db_connection)
    
    # Assert the result is an empty list
    assert result == []

def test_extract_customer_entities_null_values():
    # Mock the database connection and cursor
    mock_db_connection = Mock()
    mock_cursor = Mock()
    mock_db_connection.cursor.return_value = mock_cursor
    
    # Define data with NULL values
    mock_cursor.fetchall.return_value = [
        (3, None, 'Doe', 'doe@example.com'),
        (4, 'Jane', None, None)
    ]
    
    # Call the function
    result = extract_customer_entities(mock_db_connection)
    
    # Define the expected result
    expected_result = [
        {'customer_id': 3, 'first_name': None, 'last_name': 'Doe', 'email': 'doe@example.com'},
        {'customer_id': 4, 'first_name': 'Jane', 'last_name': None, 'email': None}
    ]
    
    # Assert the result matches the expected result
    assert result == expected_result

def test_extract_customer_entities_malformed_data():
    # Mock the database connection and cursor
    mock_db_connection = Mock()
    mock_cursor = Mock()
    mock_db_connection.cursor.return_value = mock_cursor
    
    # Define malformed data (e.g., missing fields)
    mock_cursor.fetchall.return_value = [
        (5, 'Alice'),  # Missing last_name and email
    ]
    
    # Call the function
    result = extract_customer_entities(mock_db_connection)
    
    # Define the expected result
    expected_result = [
        {'customer_id': 5, 'first_name': 'Alice', 'last_name': None, 'email': None}
    ]
    
    # Assert the result matches the expected result
    assert result == expected_result

def test_extract_customer_entities_exception_handling():
    # Mock the database connection and cursor
    mock_db_connection = Mock()
    mock_cursor = Mock()
    mock_db_connection.cursor.return_value = mock_cursor
    
    # Simulate an exception being raised
    mock_cursor.fetchall.side_effect = Exception("Database error")
    
    # Call the function
    result = extract_customer_entities(mock_db_connection)
    
    # Assert the result is an empty list due to exception handling
    assert result == []

