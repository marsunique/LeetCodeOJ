# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        stack = []
        while root:
            if root.right:
                stack.append(root.right)
                # stack right child
            if root.left:
                root.right = root.left
                # move left to right
                root.left = None
                # abort left pointer
                root = root.right
            else:
                if stack:
                    node = stack.pop()
                    root.right = node
                    root = node
                else:
                    root = None
                    
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node3.left = node1
node3.right = node4
node1.right = node2

test = Solution()
test.flatten(node3)
node = node3
while node:
    print node.val
    node = node.right
    