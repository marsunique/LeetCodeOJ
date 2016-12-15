# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        if root:
            self.res = 1
            self.dfs(root, 1)
        return self.res
    def dfs(self, root, cur):
        if root.left:
            if root.left.val - root.val == 1:
                self.dfs(root.left, cur+1)
            else:
                self.res = max(self.res, cur)
                self.dfs(root.left, 1)
        if root.right:
            if root.right.val - root.val == 1:
                self.dfs(root.right, cur+1)
            else:
                self.res = max(self.res, cur)
                self.dfs(root.right, 1)
        if not root.left and not root.right:
            self.res = max(self.res, cur)