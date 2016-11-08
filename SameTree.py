# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# DFS with stack
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        stack = [(p,q)]
        while stack:
            p, q = stack.pop()
            if p and q and p.val == q.val:
                stack.append((p.right, q.right))
                stack.append((p.left, q.left))
            elif not q and not p:
                continue
            else:
                return False
        return True
# BFS with queue
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        queue = [(p,q)]
        while queue:
            p, q = queue.pop(0)
            if p and q and p.val == q.val:
                queue.append((p.left, q.left))
                queue.append((p.right,q.right))
            elif not p and not q:
                continue
            else:
                return False
        return True
# Recursive
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p and q:
            return p.val==q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        elif not p and not q:
            return True
        else:
            return False

test = Solution()
print test.isSameTree(None, None)