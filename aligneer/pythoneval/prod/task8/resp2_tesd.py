import pytest
from unittest.mock import patch, MagicMock
from flask import Flask
from main import get_customer_by_name  # Replace 'your_module' with the actual module name

# Create a test client for the Flask app
@pytest.fixture
def app():
    app = Flask(__name__)
    return app

@pytest.fixture
def client(app):
    return app.test_client()

# Test case for a successful customer retrieval
def test_get_customer_by_name_success(client, mocker):
    mock_cursor = MagicMock()
    mock_cursor.fetchall.return_value = [
        (1, 1, 'John', 'Doe', 'john.doe@example.com', 1, True, '2021-01-01', '2021-01-02')
    ]
    
    mock_connection = MagicMock()
    mock_connection.cursor.return_value = mock_cursor
    
    mocker.patch('psycopg2.connect', return_value=mock_connection)
    
    response = get_customer_by_name('John', 'Doe')
    assert response.status_code == 200
    assert response.json == [{
        'customer_id': 1,
        'store_id': 1,
        'first_name': 'John',
        'last_name': 'Doe',
        'email': 'john.doe@example.com',
        'address_id': 1,
        'active': True,
        'create_date': '2021-01-01',
        'last_update': '2021-01-02'
    }]

# Test case for no customers found
def test_get_customer_by_name_no_customers(client, mocker):
    mock_cursor = MagicMock()
    mock_cursor.fetchall.return_value = []
    
    mock_connection = MagicMock()
    mock_connection.cursor.return_value = mock_cursor
    
    mocker.patch('psycopg2.connect', return_value=mock_connection)
    
    response = get_customer_by_name('Nonexistent', 'User')
    assert response.status_code == 404
    assert response.json == {'message': 'No customers found'}

# Test case for database connection error
def test_get_customer_by_name_db_error(client, mocker):
    mocker.patch('psycopg2.connect', side_effect=Exception('Database connection error'))
    
    response = get_customer_by_name('John', 'Doe')
    assert response.status_code == 500
    assert 'error' in response.json
    assert response.json['error'] == 'Database connection error'