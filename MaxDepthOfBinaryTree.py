# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


node1 = TreeNode()
node2 = TreeNode()
node3 = TreeNode()
node4 = TreeNode()
node5 = TreeNode()
node6 = TreeNode()
node7 = TreeNode()
node8 = TreeNode()
node9 = TreeNode()

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7
node7.right = node8
node8.left = node9
test = Solution()
print node1.left
print test.maxDepth(node1)