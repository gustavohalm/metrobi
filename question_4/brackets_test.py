import unittest
from .brackets import check_brackets


class TesFindDuplicated(unittest.TestCase):
    def test_check_brackets_true(self):
        brack = "{}[]{({})}"
        result = check_brackets(brack)
        self.assertTrue(result) 
        
    def test_check_brackets_false(self):
        brack = "{}[]}"
        result = check_brackets(brack)
        self.assertFalse(result) 
    