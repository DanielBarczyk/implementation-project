import unittest

from sample.simple import increment


class TestSimple(unittest.TestCase):

    def test_add_one(self):
        self.assertEqual(increment(5), 6)

    def test_add_one_2(self):
        self.assertEqual(increment(5), 6)


if __name__ == '__main__':
    unittest.main()
