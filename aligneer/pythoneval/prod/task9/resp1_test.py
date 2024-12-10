import pytest
from datetime import datetime
from main import transform_data

# Test fixtures for common test data
@pytest.fixture
def valid_record():
    return {
        'date': '2023-12-01',
        'amount': '100.50',
        'currency': 'usd'
    }

@pytest.fixture
def expected_valid_result():
    return {
        'date': datetime(2023, 12, 1),
        'amount': 100.50,
        'currency': 'USD'
    }

# 1. Valid Input Tests
def test_valid_input(valid_record, expected_valid_result):
    """Test transformation of valid input data"""
    result = transform_data(valid_record)
    assert result['date'] == expected_valid_result['date']
    assert result['amount'] == expected_valid_result['amount']
    assert result['currency'] == expected_valid_result['currency']

def test_valid_input_with_integer_amount():
    """Test transformation with integer amount"""
    record = {
        'date': '2023-12-01',
        'amount': '100',
        'currency': 'EUR'
    }
    result = transform_data(record)
    assert result['amount'] == 100.0
    assert isinstance(result['amount'], float)

# 2. Malformed Input Tests
@pytest.mark.parametrize("invalid_date", [
    '2023/12/01',
    '12-01-2023',
    'invalid',
    '2023-13-01',
    '2023-00-01',
])
def test_invalid_date_formats(invalid_date):
    """Test handling of various invalid date formats"""
    record = {
        'date': invalid_date,
        'amount': '100.50',
        'currency': 'USD'
    }
    assert transform_data(record) is None

@pytest.mark.parametrize("invalid_amount", [
    'abc',
    '',
    'twelve',
    '12.34.56',
    'NaN',
])
def test_invalid_amount_values(invalid_amount):
    """Test handling of invalid amount values"""
    record = {
        'date': '2023-12-01',
        'amount': invalid_amount,
        'currency': 'USD'
    }
    assert transform_data(record) is None

def test_invalid_currency_type():
    """Test handling of non-string currency value"""
    record = {
        'date': '2023-12-01',
        'amount': '100.50',
        'currency': 123  # Invalid type for currency
    }
    assert transform_data(record) is None

# 3. Missing Fields Tests
@pytest.mark.parametrize("missing_field", ['date', 'amount', 'currency'])
def test_missing_required_fields(missing_field, valid_record):
    """Test handling of missing required fields"""
    del valid_record[missing_field]
    assert transform_data(valid_record) is None

# 4. Edge Cases Tests
def test_empty_dictionary():
    """Test handling of empty dictionary"""
    assert transform_data({}) is None

def test_extra_fields(valid_record):
    """Test handling of extra fields in input"""
    valid_record['extra_field'] = 'extra_value'
    result = transform_data(valid_record)
    assert 'extra_field' in result
    assert result['extra_field'] == 'extra_value'

def test_none_input():
    """Test handling of None input"""
    assert transform_data(None) is None

@pytest.mark.parametrize("empty_value", ['', None])
def test_empty_values(empty_value, valid_record):
    """Test handling of empty or None values for each field"""
    for field in ['date', 'amount', 'currency']:
        test_record = valid_record.copy()
        test_record[field] = empty_value
        assert transform_data(test_record) is None

# 5. Boundary Value Tests
def test_extreme_amount_values():
    """Test handling of extreme numerical values"""
    large_number = {
        'date': '2023-12-01',
        'amount': '999999999999.99',
        'currency': 'USD'
    }
    result = transform_data(large_number)
    assert result['amount'] == 999999999999.99

def test_special_characters_in_currency():
    """Test handling of special characters in currency"""
    record = {
        'date': '2023-12-01',
        'amount': '100.50',
        'currency': 'us$'
    }
    result = transform_data(record)
    assert result['currency'] == 'US$'
