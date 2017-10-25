# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Better Version, O(N)
class Solution(object):
    # both subtrees of a node have to be balanced 
    # and depth of both subtrees never differ more than 1
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.check(root) != -1

    def check(self, root):
        '''
        combine calculate depth of a tree (subtree) and examine whether
        subtrees are balanced together. If return -1 means current node 
        is not balanced, else return actual height of this node
        '''
        if not root:
            return 0
        else:
            left = self.check(root.left)
            right = self.check(root.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            else:
                return max(left, right) + 1


# Worse Version, O(N^2)
class Solution(object):
    # both subtrees of a node have to be balanced 
    # and depth of both subtrees never differ more than 1
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        else:
            if abs(self.depthOf(root.left) - self.depthOf(root.right)) <= 1\
            and self.isBalanced(root.left) and self.isBalanced(root.right):
                return True
            else:
                return False

    def depthOf(self, node):
        if not node:
            return 0
        return max(self.depthOf(node.left), self.depthOf(node.right))+1
