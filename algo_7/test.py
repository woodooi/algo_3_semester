import unittest
from igones import Indiana, read

class TestIndiana(unittest.TestCase):
    def test_all_exits_single_row(self):
        with open('test1', 'r') as file:
            file_content = file.readlines()

        H, W, corridor = read(file_content)
        indiana = Indiana(H, W, corridor)
        result = indiana.all_exits()
        self.assertEqual(result, 2)

    def test_all_exits_multiple_rows(self):
        with open('test2', 'r') as file:
            file_content = file.readlines()

        H, W, corridor = read(file_content)
        indiana = Indiana(H, W, corridor)
        result = indiana.all_exits()
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()