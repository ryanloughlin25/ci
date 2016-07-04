import unittest
from foo import sign


class TestSign(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(sign(5), 'positive')


if __name__ == '__main__':
    unittest.main()
