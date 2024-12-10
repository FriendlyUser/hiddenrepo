import pytest
import psycopg2
from unittest.mock import patch, MagicMock
from datetime import datetime, timedelta
import logging
from main import monitor_and_log_unrented_films

@pytest.fixture
def mock_db_connection():
    """Fixture to mock database connection and cursor"""
    with patch('psycopg2.connect') as mock_connect:
        mock_cursor = MagicMock()
        mock_connect.return_value.cursor.return_value = mock_cursor
        yield mock_connect, mock_cursor

@pytest.fixture
def mock_logging():
    """Fixture to mock logging"""
    with patch('logging.info') as mock_info, patch('logging.error') as mock_error:
        yield mock_info, mock_error

def test_successful_execution(mock_db_connection, mock_logging):
    """Test successful execution with unrented films"""
    mock_connect, mock_cursor = mock_db_connection
    mock_info, mock_error = mock_logging
    
    # Mock data for unrented films
    mock_cursor.fetchall.return_value = [
        (1, "Film 1", None),
        (2, "Film 2", datetime.now() - timedelta(days=400))
    ]
    
    monitor_and_log_unrented_films()
    
    # Verify database operations
    assert mock_cursor.execute.called
    assert mock_cursor.close.called
    assert mock_connect.return_value.close.called
    
    # Verify logging calls
    assert mock_info.call_count == 2
    assert "Film ID: 1" in mock_info.call_args_list[0][0][0]
    assert "Film ID: 2" in mock_info.call_args_list[1][0][0]

def test_database_connection_failure(mock_db_connection, mock_logging):
    """Test handling of database connection failure"""
    mock_connect, _ = mock_db_connection
    mock_info, mock_error = mock_logging
    
    mock_connect.side_effect = Exception("Connection failed")
    
    monitor_and_log_unrented_films()
    
    mock_error.assert_called_once()
    assert "Connection failed" in mock_error.call_args[0][0]

def test_query_execution_error(mock_db_connection, mock_logging):
    """Test handling of query execution error"""
    mock_connect, mock_cursor = mock_db_connection
    mock_info, mock_error = mock_logging
    
    mock_cursor.execute.side_effect = Exception("Query failed")
    
    monitor_and_log_unrented_films()
    
    mock_error.assert_called_once()
    assert "Query failed" in mock_error.call_args[0][0]

def test_empty_result_set(mock_db_connection, mock_logging):
    """Test behavior when no unrented films are found"""
    mock_connect, mock_cursor = mock_db_connection
    mock_info, mock_error = mock_logging
    
    mock_cursor.fetchall.return_value = []
    
    monitor_and_log_unrented_films()
    
    assert not mock_info.called
    assert not mock_error.called

def test_null_values_in_result(mock_db_connection, mock_logging):
    """Test handling of NULL values in the result set"""
    mock_connect, mock_cursor = mock_db_connection
    mock_info, mock_error = mock_logging
    
    mock_cursor.fetchall.return_value = [
        (None, None, None),
        (1, "Film 1", None)
    ]
    
    monitor_and_log_unrented_films()
    
    assert mock_info.call_count == 2
    assert "None" in mock_info.call_args_list[0][0][0]

@pytest.mark.parametrize("exception_type", [
    psycopg2.OperationalError,
    psycopg2.ProgrammingError,
    psycopg2.InternalError
])
def test_specific_database_exceptions(mock_db_connection, mock_logging, exception_type):
    """Test handling of specific database exceptions"""
    mock_connect, _ = mock_db_connection
    mock_info, mock_error = mock_logging
    
    mock_connect.side_effect = exception_type("Database error")
    
    monitor_and_log_unrented_films()
    
    mock_error.assert_called_once()
    assert "Database error" in mock_error.call_args[0][0]

def test_cursor_cleanup_on_error(mock_db_connection, mock_logging):
    """Test proper cleanup of database resources on error"""
    mock_connect, mock_cursor = mock_db_connection
    mock_info, mock_error = mock_logging
    
    mock_cursor.execute.side_effect = Exception("Query failed")
    
    monitor_and_log_unrented_films()
    
    mock_cursor.close.assert_called_once()
    mock_connect.return_value.close.assert_called_once()