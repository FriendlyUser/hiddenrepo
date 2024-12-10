import pytest
from unittest.mock import patch, MagicMock
from datetime import datetime
from main import app, get_customer_by_name
import psycopg2

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# Sample customer data for testing
@pytest.fixture
def sample_customer():
    return (
        1,              # customer_id
        1,              # store_id
        'MARY',         # first_name
        'SMITH',        # last_name
        'mary.smith@example.com',  # email
        5,              # address_id
        True,           # active
        datetime.now(), # create_date
        datetime.now()  # last_update
    )

def test_successful_customer_retrieval(client, sample_customer):
    """Test successful customer retrieval with valid name"""
    with patch('psycopg2.connect') as mock_connect:
        # Setup mock cursor and connection
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [sample_customer]
        mock_connect.return_value.cursor.return_value = mock_cursor

        response = get_customer_by_name('MARY', 'SMITH')
        data = response.get_json()

        assert response.status_code == 200
        assert len(data) == 1
        assert data[0]['first_name'] == 'MARY'
        assert data[0]['last_name'] == 'SMITH'
        assert data[0]['email'] == 'mary.smith@example.com'

def test_customer_not_found(client):
    """Test when no customer is found"""
    with patch('psycopg2.connect') as mock_connect:
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = []
        mock_connect.return_value.cursor.return_value = mock_cursor

        response = get_customer_by_name('NONEXISTENT', 'CUSTOMER')
        data = response.get_json()

        assert response.status_code == 404
        assert data['message'] == 'No customers found'

def test_database_connection_error(client):
    """Test database connection error"""
    with patch('psycopg2.connect') as mock_connect:
        mock_connect.side_effect = psycopg2.Error("Connection error")

        response = get_customer_by_name('MARY', 'SMITH')
        data = response.get_json()

        assert response.status_code == 500
        assert 'error' in data

def test_multiple_customers_same_name(client, sample_customer):
    """Test multiple customers with same name"""
    with patch('psycopg2.connect') as mock_connect:
        mock_cursor = MagicMock()
        # Create two customers with same name but different IDs
        customer1 = sample_customer
        customer2 = (2,) + sample_customer[1:]
        mock_cursor.fetchall.return_value = [customer1, customer2]
        mock_connect.return_value.cursor.return_value = mock_cursor

        response = get_customer_by_name('MARY', 'SMITH')
        data = response.get_json()

        assert response.status_code == 200
        assert len(data) == 2
        assert data[0]['customer_id'] != data[1]['customer_id']
        assert data[0]['first_name'] == data[1]['first_name']
        assert data[0]['last_name'] == data[1]['last_name']

def test_sql_injection_attempt(client):
    """Test SQL injection prevention"""
    with patch('psycopg2.connect') as mock_connect:
        mock_cursor = MagicMock()
        mock_cursor.execute.side_effect = psycopg2.Error("SQL Injection attempted")
        mock_connect.return_value.cursor.return_value = mock_cursor

        response = get_customer_by_name("'; DROP TABLE customer; --", 'SMITH')
        data = response.get_json()

        assert response.status_code == 500
        assert 'error' in data

def test_null_parameters(client):
    """Test handling of NULL parameters"""
    with patch('psycopg2.connect') as mock_connect:
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = []
        mock_connect.return_value.cursor.return_value = mock_cursor

        response = get_customer_by_name(None, None)
        data = response.get_json()

        assert response.status_code == 404
        assert data['message'] == 'No customers found'

def test_cursor_close_on_error(client):
    """Test cursor and connection are closed even when error occurs"""
    mock_cursor = MagicMock()
    mock_connection = MagicMock()
    
    with patch('psycopg2.connect') as mock_connect:
        mock_connect.return_value = mock_connection
        mock_connection.cursor.return_value = mock_cursor
        mock_cursor.execute.side_effect = Exception("Test error")

        response = get_customer_by_name('MARY', 'SMITH')

        mock_cursor.close.assert_called_once()
        mock_connection.close.assert_called_once()
