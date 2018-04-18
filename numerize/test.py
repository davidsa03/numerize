import unittest
from numerize import numerize

class TestNumberMethods(unittest.TestCase):

    def testUnderThousand(self):
        for i in range(999):
            self.assertEqual(numerize(i), str(i))

    def testThousand(self):
        self.assertEqual(numerize(1000), '1K')
        self.assertEqual(numerize(-1000), '-1K')
        self.assertEqual(numerize(1100), '1.1K')
        self.assertEqual(numerize(-1100), '-1.1K')
        self.assertEqual(numerize(10000), '10K')
        self.assertEqual(numerize(-10000), '-10K')
        self.assertEqual(numerize(100000), '100K')
        self.assertEqual(numerize(-100000), '-100K')

    def testMillion(self):
        self.assertEqual(numerize(1000000), '1M')
        self.assertEqual(numerize(-1000000), '-1M')
        self.assertEqual(numerize(1100000), '1.1M')
        self.assertEqual(numerize(-1100000), '-1.1M')
        self.assertEqual(numerize(10000000), '10M')
        self.assertEqual(numerize(-10000000), '-10M')
        self.assertEqual(numerize(100000000), '100M')
        self.assertEqual(numerize(-100000000), '-100M')

    def testBillion(self):
        self.assertEqual(numerize(1000000000), '1B')
        self.assertEqual(numerize(-1000000000), '-1B')
        self.assertEqual(numerize(1100000000), '1.1B')
        self.assertEqual(numerize(-1100000000), '-1.1B')
        self.assertEqual(numerize(10000000000), '10B')
        self.assertEqual(numerize(-10000000000), '-10B')
        self.assertEqual(numerize(100000000000), '100B')
        self.assertEqual(numerize(-100000000000), '-100B')

    def testTrillion(self):
        self.assertEqual(numerize(1000000000000), '1T')
        self.assertEqual(numerize(-1000000000000), '-1T')
        self.assertEqual(numerize(1100000000000), '1.1T')
        self.assertEqual(numerize(-1100000000000), '-1.1T')
        self.assertEqual(numerize(10000000000000), '10T')
        self.assertEqual(numerize(-10000000000000), '-10T')
        self.assertEqual(numerize(100000000000000), '100T')
        self.assertEqual(numerize(-100000000000000), '-100T')

    def testDecimal(self):
        self.assertEqual(numerize(1.0), '1')
        self.assertEqual(numerize(-1.0), '-1')
        self.assertEqual(numerize(1.1), '1.1')
        self.assertEqual(numerize(-1.1), '-1.1')
        self.assertEqual(numerize(1.10), '1.1')
        self.assertEqual(numerize(-1.10), '-1.1')
        self.assertEqual(numerize(1.11), '1.11')
        self.assertEqual(numerize(-1.11), '-1.11')
        self.assertEqual(numerize(1.111), '1.11')
        self.assertEqual(numerize(-1.111), '-1.11')

    def testDecimalParam(self):
        self.assertEqual(numerize(1), '1')
        self.assertEqual(numerize(1.23), '1.23')
        self.assertEqual(numerize(1.23, 3), '1.23')
        self.assertEqual(numerize(1.234, 3), '1.234')
        self.assertEqual(numerize(1.2345, 4), '1.2345')

    def testBounds(self):
        self.assertEqual(numerize(1000000000000000), '1000000000000000')
        self.assertEqual(numerize(-1000000000000000), '-1000000000000000')

def main():
    unittest.main()

if __name__ == '__main__':
    main()
