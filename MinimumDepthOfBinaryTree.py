# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        if left and right:
            return 1+min(left, right)
        else:
            # at least one of them is 0, 1+left+right is equivalent to
            # 1+left or 1+right or 1
            return 1 + right + left
