class TreeNode:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def find_last_left_child(node):
    if not node:
        return None
    while node.left:
        node = node.left
    return node

def in_order_successor(root, target):
    if not root or not target:
        return None
    
    if target.right:
        return find_last_left_child(target.right)
    
    if target.parent and target == target.parent.left:
        return target.parent

    while target.parent and target == target.parent.right:
        target = target.parent

    return target.parent

root = TreeNode(1)
root.left = TreeNode(2)
root.left.parent = root
root.right = TreeNode(3)
root.right.parent = root
root.left.left = TreeNode(4)
root.left.left.parent = root.left
root.left.right = TreeNode(5)
root.left.right.parent = root.left

target_node = root.left.left 

successor = in_order_successor(root, target_node)

if successor:
    print("In-order successor of the target node is:", successor.value)
else:
    print("Target node does not have an in-order successor.")
