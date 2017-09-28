# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# recursive
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.helper(root.left, root.right)
    
    def helper(self, lnode, rnode):
        if (not lnode) and (not rnode):
            return True
        elif (lnode and rnode) and (lnode.val == rnode.val):
            return self.helper(lnode.left, rnode.right) and self.helper(lnode.right, rnode.left)
        else:
            return False
