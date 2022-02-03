import imp
import unittest
from .duplicated import find_duplicated


class TesFindDuplicated(unittest.TestCase):
    def test_simple_duplicated(self):
        arr_test = [1, 3, 4, 2, 1, 5, 0,2]
        arr_result = [1, 2]
        result = find_duplicated(arr_test)
        self.assertEqual(result, arr_result)

    def test_multiple_duplicated(self):
        arr_test = [1, 3, 4, 2, 1, 5, 0,2, 3, 2, 2, 3, 4]
        arr_result = [1, 2, 3, 4]
        result = find_duplicated(arr_test)
        self.assertEqual(result, arr_result)
        