import unittest
from main import process_data

class TestProcessData(unittest.TestCase):
    def test_simple_values(self):
        data = [
            {'value': 1.0},
            {'value': 2.0},
            {'value': 3.0}
        ]
        expected = {'total': 6.0, 'average': 2.0, 'count': 3}
        self.assertEqual(process_data(data), expected)

    def test_nested_dict_values(self):
        data = [
            {'value': {'nested_value': 1.0}},
            {'value': {'nested_value': 2.0}}
        ]
        expected = {'total': 3.0, 'average': 1.5, 'count': 2}
        self.assertEqual(process_data(data), expected)

    def test_nested_list_values(self):
        data = [
            {'value': {'nested_value': [1.0, 2.0]}},
            {'value': {'nested_value': [3.0, 4.0]}}
        ]
        expected = {'total': 10.0, 'average': 5.0, 'count': 2}
        self.assertEqual(process_data(data), expected)

    def test_list_values(self):
        data = [
            {'value': [1.0, 2.0]},
            {'value': [3.0, 4.0]}
        ]
        expected = {'total': 10.0, 'average': 2.5, 'count': 4}
        self.assertEqual(process_data(data), expected)

    def test_missing_values(self):
        data = [
            {},
            {'value': None},
            {'value': 1.0}
        ]
        expected = {'total': 1.0, 'average': 1.0, 'count': 1}
        self.assertEqual(process_data(data), expected)

    def test_invalid_values(self):
        data = [
            {'value': 'not_a_number'},
            {'value': 1.0},
            {'value': [1.0, 'invalid', 2.0]}
        ]
        expected = {'total': 4.0, 'average': 1.333333333333333, 'count': 3}
        self.assertEqual(process_data(data), expected)

    def test_empty_input(self):
        data = []
        expected = {'total': 0.0, 'average': 0.0, 'count': 0}
        self.assertEqual(process_data(data), expected)

    def test_mixed_types(self):
        data = [
            {'value': 1},
            {'value': '2.0'},
            {'value': 3.0}
        ]
        expected = {'total': 6.0, 'average': 2.0, 'count': 3}
        self.assertEqual(process_data(data), expected)

    def test_nested_empty_structures(self):
        data = [
            {'value': {}},
            {'value': []},
            {'value': {'nested_value': []}},
            {'value': {'nested_value': {}}}
        ]
        expected = {'total': 0.0, 'average': 0.0, 'count': 0}
        self.assertEqual(process_data(data), expected)

if __name__ == '__main__':
    unittest.main()
