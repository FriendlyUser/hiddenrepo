import pytest
from unittest.mock import patch, MagicMock
import logging
from main import monitor_and_log_unrented_films  # Replace with the actual module name

# Test for database connection failure
@patch('psycopg2.connect')
def test_database_connection_failure(mock_connect):
    mock_connect.side_effect = Exception("Connection failed")
    with patch('logging.error') as mock_logging_error:
        monitor_and_log_unrented_films()
        mock_logging_error.assert_called_with("An error occurred: Connection failed")

# Test for query execution errors
@patch('psycopg2.connect')
def test_query_execution_error(mock_connect):
    mock_conn = MagicMock()
    mock_cursor = mock_conn.cursor.return_value
    mock_cursor.execute.side_effect = Exception("Query execution failed")
    mock_connect.return_value = mock_conn

    with patch('logging.error') as mock_logging_error:
        monitor_and_log_unrented_films()
        mock_logging_error.assert_called_with("An error occurred: Query execution failed")

# Test for handling films that have never been rented
@patch('psycopg2.connect')
def test_films_never_rented(mock_connect):
    mock_conn = MagicMock()
    mock_cursor = mock_conn.cursor.return_value
    mock_cursor.fetchall.return_value = [(1, 'Film A', None), (2, 'Film B', None)]
    mock_connect.return_value = mock_conn

    with patch('logging.info') as mock_logging_info:
        monitor_and_log_unrented_films()
        mock_logging_info.assert_any_call("Film ID: 1, Title: Film A, Last Rented: None")
        mock_logging_info.assert_any_call("Film ID: 2, Title: Film B, Last Rented: None")

# Test for empty film table or missing columns
@patch('psycopg2.connect')
def test_empty_film_table(mock_connect):
    mock_conn = MagicMock()
    mock_cursor = mock_conn.cursor.return_value
    mock_cursor.fetchall.return_value = []
    mock_connect.return_value = mock_conn

    with patch('logging.info') as mock_logging_info:
        monitor_and_log_unrented_films()
        mock_logging_info.assert_not_called()

# Test for logging behavior
@patch('psycopg2.connect')
def test_logging_behavior(mock_connect):
    mock_conn = MagicMock()
    mock_cursor = mock_conn.cursor.return_value
    mock_cursor.fetchall.return_value = [(1, 'Film A', '2022-01-01')]
    mock_connect.return_value = mock_conn

    with patch('logging.info') as mock_logging_info:
        monitor_and_log_unrented_films()
        mock_logging_info.assert_called_with("Film ID: 1, Title: Film A, Last Rented: 2022-01-01")
