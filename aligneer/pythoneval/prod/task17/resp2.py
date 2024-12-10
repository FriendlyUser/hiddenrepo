import unittest
from main import process_data

class TestProcessData(unittest.TestCase):
    def test_empty_list(self):
        data = []
        result = process_data(data)
        self.assertEqual(result, {'total': 0.0, 'average': 0.0, 'count': 0})

    def test_missing_value_key(self):
        data = [{'other_key': 10}]
        result = process_data(data)
        self.assertEqual(result, {'total': 0.0, 'average': 0.0, 'count': 0})

    def test_non_numeric_values(self):
        data = [{'value': 'abc'}, {'value': {'nested_value': ['xyz']}}]
        result = process_data(data)
        self.assertEqual(result, {'total': 0.0, 'average': 0.0, 'count': 0})

    def test_nested_dictionaries(self):
        data = [{'value': {'nested_value': [1, 2, 3]}}]
        result = process_data(data)
        self.assertEqual(result, {'total': 6.0, 'average': 6.0, 'count': 1})

    def test_lists_of_numbers(self):
        data = [{'value': [1, 2, 3]}]
        result = process_data(data)
        self.assertEqual(result, {'total': 6.0, 'average': 2.0, 'count': 3})

    def test_mixed_types(self):
        data = [{'value': 1}, {'value': [2, 'a']}, {'value': {'nested_value': 3}}]
        result = process_data(data)
        self.assertEqual(result, {'total': 6.0, 'average': 2.0, 'count': 3})

    def test_large_numbers(self):
        data = [{'value': 1e10}, {'value': [1e10, 1e10]}]
        result = process_data(data)
        self.assertEqual(result, {'total': 3e10, 'average': 1e10, 'count': 3})

    def test_negative_numbers(self):
        data = [{'value': -1}, {'value': [-2, -3]}]
        result = process_data(data)
        self.assertEqual(result, {'total': -6.0, 'average': -2.0, 'count': 3})

    def test_single_element(self):
        data = [{'value': 5}]
        result = process_data(data)
        self.assertEqual(result, {'total': 5.0, 'average': 5.0, 'count': 1})

    def test_nested_lists(self):
        data = [{'value': [[1, 2], 3]}]
        result = process_data(data)
        self.assertEqual(result, {'total': 3.0, 'average': 1.5, 'count': 2})

if __name__ == '__main__':
    unittest.main()
