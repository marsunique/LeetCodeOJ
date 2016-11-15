# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Preorder
def preorder(root):
    res = []
    stack = []
    while stack or root:
        if root:
            res.append(root.val)
            stack.append(root)
            root = root.left
        else:
            node = stack.pop()
            root = node.right
    return res

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7

print preorder(node1)
