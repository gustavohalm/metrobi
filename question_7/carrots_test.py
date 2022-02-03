import unittest
from .carrots import check_carrots


class TesFindDuplicated(unittest.TestCase):
    def test_carrots_max(self):
        capability = 36
        carrs =[ {
            'kg': 10,
            'price': 100
        }, {
            'kg': 12,
            'price': 300
        },{
            'kg': 11,
            'price': 200
        },
        {
            'kg': 100,
            'price': 104
        },
        ]
        result = check_carrots(carrs, capability)
        expected = {
            'kg': 33,
            'price': 600
        }
        self.assertEqual(result, expected)