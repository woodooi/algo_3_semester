import unittest
from algo_lab_1 import Solution

class TestZigzagTraversal(unittest.TestCase):

    def test_square_matrix(self):
        matrix = Solution([
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ])
        expected_result = [1, 2, 6, 11, 7, 3, 4, 8, 12, 16, 21, 17, 13, 9, 5, 10, 14, 18, 22, 23, 19, 15, 20, 24, 25]
        self.assertEqual(matrix.zig_zagging(), expected_result)

    def test_non_square_matrix(self):
        matrix = Solution([
            [1, 2],
            [3, 4],
            [5, 6],
            [7, 8]
        ])
        expected_result = [1, 2, 3, 5, 4, 6, 7, 8]
        self.assertEqual(matrix.zig_zagging(), expected_result)

    def test_single_element_matrix(self):
        matrix = Solution([[9]])
        expected_result = [9]
        self.assertEqual(matrix.zig_zagging(), expected_result)

    def test_1x6_matrix(self):
        matrix = Solution([[1, 2, 3, 4, 5, 6]])
        expected_result = [1, 2, 3, 4, 5, 6]
        self.assertEqual(matrix.zig_zagging(), expected_result)

    def test_1x1_matrix(self):
        matrix = Solution([[7]])
        expected_result = [7]
        self.assertEqual(matrix.zig_zagging(), expected_result)

if __name__ == '__main__':
    unittest.main()
