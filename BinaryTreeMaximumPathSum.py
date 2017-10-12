# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maximum = -float('inf')
        self.dfs(root)
        return self.maximum
        
    def dfs(self, node):
        if not node:
            return 0
        l_max = self.dfs(node.left)
        r_max = self.dfs(node.right)
        self.maximum = max(self.maximum, l_max + r_max + node.val)
        return max(0, node.val + max(l_max, r_max))

test = Solution()
test.maxPathSum()