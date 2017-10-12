# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        return self.dfs(t)

    def dfs(self, node):
        if not node:
            return ''
        s_left = self.dfs(node.left)
        s_right = self.dfs(node.right)
        if s_right:
            return str(node.val) + '(' + s_left + ')' + '(' + s_right + ')'
        elif s_left:
            return str(node.val) + '(' + s_left + ')'
        else:
            return str(node.val)
