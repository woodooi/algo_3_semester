import unittest
from hamsters import how_much_hamsters_can_you_handle_subtract


class TestHamsterHandling(unittest.TestCase):

    def test_valid_case(self):
        food = 7
        number_of_hams = 3
        hams = [[1, 2], [2, 2], [3, 1]]
        result = how_much_hamsters_can_you_handle_subtract(food, number_of_hams, hams)
        self.assertEqual(result, 2)

    def test_second_case(self):
        food = 19
        number_of_hams = 4
        hams = [[5, 0], [2, 2], [1, 4], [5, 1]]
        result = how_much_hamsters_can_you_handle_subtract(food, number_of_hams, hams)
        self.assertEqual(result, 3)

    def test_third_case(self):
        food = 2
        number = 2
        hams = [[1, 500000], [1, 60000]]
        result = how_much_hamsters_can_you_handle_subtract(food, number, hams)
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()
