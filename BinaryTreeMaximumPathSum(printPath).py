# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maximum = -float('inf')
        self.path = ''
        self.dfs(root)
        print 'path:', self.path
        print 'value:', self.maximum
        
    def dfs(self, node):
        if not node:
            return (0, '')
        l_max = self.dfs(node.left)
        r_max = self.dfs(node.right)
        if l_max[0] + r_max[0] + node.val > self.maximum:
            self.maximum = l_max[0] + r_max[0] + node.val
            self.path = l_max[1] + str(node.val) + r_max[1][::-1]

        if node.val + l_max[0] > node.val + r_max[0]:
            if node.val + l_max[0] > 0:
                return (node.val + l_max[0], l_max[1] + str(node.val))
            else:
                return (0, '')
        else:
            if node.val + r_max[0] > 0:
                return (node.val + r_max[0], r_max[1] + str(node.val))
            else:
                return (0, '')


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7
test = Solution()
test.maxPathSum(node1)
