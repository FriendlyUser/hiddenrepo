import pytest
from unittest.mock import Mock, patch
import psycopg2
from psycopg2.extensions import cursor
from db import extract_customer_entities

@pytest.fixture
def mock_db_connection():
    """Fixture to create a mock database connection"""
    mock_conn = Mock()
    mock_cursor = Mock()
    mock_conn.cursor.return_value = mock_cursor
    return mock_conn, mock_cursor

def test_successful_extraction(mock_db_connection):
    """Test successful extraction of customer data"""
    mock_conn, mock_cursor = mock_db_connection
    
    # Mock data that would come from database
    mock_cursor.fetchall.return_value = [
        (1, "John", "Doe", "john@example.com"),
        (2, "Jane", "Smith", "jane@example.com")
    ]
    
    expected_result = [
        {
            'customer_id': 1,
            'first_name': "John",
            'last_name': "Doe",
            'email': "john@example.com"
        },
        {
            'customer_id': 2,
            'first_name': "Jane",
            'last_name': "Smith",
            'email': "jane@example.com"
        }
    ]
    
    result = extract_customer_entities(mock_conn)
    assert result == expected_result

def test_empty_result_set(mock_db_connection):
    """Test handling of empty result set"""
    mock_conn, mock_cursor = mock_db_connection
    mock_cursor.fetchall.return_value = []
    
    result = extract_customer_entities(mock_conn)
    assert result == []

def test_null_values(mock_db_connection):
    """Test handling of NULL values in database results"""
    mock_conn, mock_cursor = mock_db_connection
    mock_cursor.fetchall.return_value = [
        (1, None, "Doe", None),
        (2, "Jane", None, "jane@example.com")
    ]
    
    expected_result = [
        {
            'customer_id': 1,
            'first_name': None,
            'last_name': "Doe",
            'email': None
        },
        {
            'customer_id': 2,
            'first_name': "Jane",
            'last_name': None,
            'email': "jane@example.com"
        }
    ]
    
    result = extract_customer_entities(mock_conn)
    assert result == expected_result

def test_database_error(mock_db_connection):
    """Test handling of database errors"""
    mock_conn, mock_cursor = mock_db_connection
    mock_cursor.execute.side_effect = psycopg2.Error("Database error")
    
    result = extract_customer_entities(mock_conn)
    assert result == []

def test_malformed_data(mock_db_connection):
    """Test handling of malformed data (incorrect number of columns)"""
    mock_conn, mock_cursor = mock_db_connection
    mock_cursor.fetchall.return_value = [
        (1, "John"),  # Missing columns
        (2, "Jane", "Smith", "jane@example.com", "extra")  # Extra column
    ]
    
    with pytest.raises(IndexError):
        result = extract_customer_entities(mock_conn)

def test_invalid_data_types(mock_db_connection):
    """Test handling of invalid data types"""
    mock_conn, mock_cursor = mock_db_connection
    mock_cursor.fetchall.return_value = [
        (1, 123, "Doe", "john@example.com"),  # first_name as integer
        ("invalid", "Jane", "Smith", "jane@example.com")  # customer_id as string
    ]
    
    result = extract_customer_entities(mock_conn)
    expected_result = [
        {
            'customer_id': 1,
            'first_name': 123,
            'last_name': "Doe",
            'email': "john@example.com"
        },
        {
            'customer_id': "invalid",
            'first_name': "Jane",
            'last_name': "Smith",
            'email': "jane@example.com"
        }
    ]
    assert result == expected_result

@pytest.mark.parametrize("mock_exception", [
    ValueError("Value error"),
    TypeError("Type error"),
    Exception("Generic error")
])
def test_various_exceptions(mock_db_connection, mock_exception):
    """Test handling of various types of exceptions"""
    mock_conn, mock_cursor = mock_db_connection
    mock_cursor.execute.side_effect = mock_exception
    
    result = extract_customer_entities(mock_conn)
    assert result == []