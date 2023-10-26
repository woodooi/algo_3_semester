import unittest
from binary3 import TreeNode
from binary3 import in_order_successor
from binary3 import find_last_left_child

class TestInOrderSuccessor(unittest.TestCase):
    def test_in_order_successor(self):

        root = TreeNode(10)
        root.left = TreeNode(5)
        root.right = TreeNode(15)
        root.left.parent = root
        root.right.parent = root

        root.left.left = TreeNode(3)
        root.left.right = TreeNode(7)
        root.left.left.parent = root.left
        root.left.right.parent = root.left

        
        self.assertIsNone(in_order_successor(root, None)) 

        
        self.assertEqual(in_order_successor(root, root.left.left), root.left) 
        self.assertEqual(in_order_successor(root, root.left.right), root) 
        self.assertEqual(in_order_successor(root, root.right), None) 

        
        self.assertEqual(in_order_successor(root, root.left), root.left.right)  
        self.assertEqual(in_order_successor(root, root), find_last_left_child(root.right))  

if __name__ == "__main__":
    unittest.main()
