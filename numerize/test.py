import unittest
from numerize import numerize
class TestNumerizeFunc(unittest.TestCase):
    def test_numerize(self):
        self.assertEqual(numerize(1), "1")
        self.assertEqual(numerize(10), "10")
    def test_thousand(self):
        self.assertEqual(numerize(1000), "1K")
    def test_strict(self):
        self.assertEqual(numerize(999), "999")
        self.assertEqual(numerize(9999), "10.00K")
    def test_negative(self): 
        self.assertEqual(numerize(-1), "-1")
        self.assertEqual(numerize(-10), "-10")
        self.assertEqual(numerize(-1000), "-1K")
        self.assertEqual(numerize(-9999,4), "-9.9990K")

if __name__ == '__main__':
    unittest.main()