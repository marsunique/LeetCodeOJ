# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        # nodes can contain negative value
        if not root:
            return False
        return self.hasPath(root, sum)

    def hasPath(self, root, remain):
        # if hit NULL node, means its parent node has one child node,
        # therefore this is not a path to the leaf
        if not root:
            return False
        # leaf node
        if not root.left and not root.right:
            if remain == root.val:
                return True
            return False
        return self.hasPath(root.left, remain-root.val) or self.hasPath(root.right, remain-root.val)