import unittest

from price import price


class TestPrice(unittest.TestCase):

    def test_basics(self):
        self.assertEqual(0, price([]))
        self.assertEqual(8, price([1]))
        self.assertEqual(8, price([2]))
        self.assertEqual(8, price([3]))
        self.assertEqual(8, price([4]))
        self.assertEqual(8 * 3, price([1, 1, 1]))

    def test_simple_discounts(self):
        self.assertEqual(8 * 2 * 0.95, price([0, 1]))
        self.assertEqual(8 * 3 * 0.9, price([0, 2, 4]))
        self.assertEqual(8 * 4 * 0.8, price([0, 1, 2, 4]))
        self.assertEqual(8 * 5 * 0.75, price([0, 1, 2, 3, 4]))

    def test_several_discounts(self):
        self.assertEqual(8 + (8 * 2 * 0.95), price([0, 0, 1]))
        self.assertEqual(2 * (8 * 2 * 0.95), price([0, 0, 1, 1]))
        self.assertEqual((8 * 4 * 0.8) + (8 * 2 * 0.95), price([0, 0, 1, 2, 2, 3]))
        self.assertEqual(8 + (8 * 5 * 0.75), price([0, 1, 1, 2, 3, 4]))

    def test_edge_cases(self):
        self.assertEqual(2 * (8 * 4 * 0.8), price([0, 0, 1, 1, 2, 2, 3, 4]))
        self.assertEqual(3 * (8 * 5 * 0.75) + 2 * (8 * 4 * 0.8),
                         price([0, 0, 0, 0, 0,
                                1, 1, 1, 1, 1,
                                2, 2, 2, 2,
                                3, 3, 3, 3, 3,
                                4, 4, 4, 4]))


if __name__ == "__main__":
    unittest.main()

if __name__ == '__main__':
    unittest.main()
