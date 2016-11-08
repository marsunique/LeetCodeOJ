# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if not root:
            return res
        queue = [[root]]
        res = [[root.val]]
        while queue:
            queue = [[node.left, node.right] for pair in queue for node in pair if node]
            temp = [child.val for pair in queue for child in pair if child]
            if len(temp):
                res.insert(0,temp)
        return res