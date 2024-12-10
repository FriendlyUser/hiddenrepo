import pytest
from datetime import datetime
from main import transform_data  # Replace 'your_module' with the actual module name

def test_valid_input():
    record = {
        'date': '2023-10-01',
        'amount': '100.50',
        'currency': 'usd'
    }
    expected = {
        'date': datetime(2023, 10, 1),
        'amount': 100.50,
        'currency': 'USD'
    }
    assert transform_data(record) == expected

def test_invalid_date_format():
    record = {
        'date': '01-10-2023',
        'amount': '100.50',
        'currency': 'usd'
    }
    assert transform_data(record) is None

def test_non_numeric_amount():
    record = {
        'date': '2023-10-01',
        'amount': 'one hundred',
        'currency': 'usd'
    }
    assert transform_data(record) is None

def test_missing_currency():
    record = {
        'date': '2023-10-01',
        'amount': '100.50'
    }
    assert transform_data(record) is None

def test_empty_dictionary():
    record = {}
    assert transform_data(record) is None

def test_extra_fields():
    record = {
        'date': '2023-10-01',
        'amount': '100.50',
        'currency': 'usd',
        'extra_field': 'extra_value'
    }
    expected = {
        'date': datetime(2023, 10, 1),
        'amount': 100.50,
        'currency': 'USD'
    }
    assert transform_data(record) == expected

def test_completely_invalid_values():
    record = {
        'date': None,
        'amount': None,
        'currency': None
    }
    assert transform_data(record) is None

def test_missing_date():
    record = {
        'amount': '100.50',
        'currency': 'usd'
    }
    assert transform_data(record) is None

def test_missing_amount():
    record = {
        'date': '2023-10-01',
        'currency': 'usd'
    }
    assert transform_data(record) is None

def test_empty_values():
    record = {
        'date': '',
        'amount': '',
        'currency': ''
    }
    assert transform_data(record) is None
