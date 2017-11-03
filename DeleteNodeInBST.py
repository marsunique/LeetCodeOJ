# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return None
        if root.val < key:
            root.left = self.deleteNode(root.left, key)
        elif root.val > key:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left and not root.right:
                return None
            elif not root.left:
                return root.right
            elif not root.right:
                return root.left:
            else:
                minNode = self.finMin(root.right)
                root.val = minNode.val
                root.right = self.deleteNode(root.right, minNode.val)
        return root

    def finMin(self, root):
        while root.left:
            root = root.left
        return root
