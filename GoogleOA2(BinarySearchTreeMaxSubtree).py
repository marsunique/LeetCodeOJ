class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.currentMax = 0
    def maxSubtree(self, root, minimum, maximum):
        if not root:
            return 0
        self.dfs(root, minimum, maximum)
        return self.currentMax
    def dfs(self, root, minimum, maximum):
        if root:
            left = self.dfs(root.left, minimum, maximum)
            right = self.dfs(root.right, minimum, maximum)
            print 'val:', root.val, 'left:', left, 'right:', right
            if (left == -1 or right == -1) and root.val >= minimum and root.val <= maximum:
                # at least one child is None and root.val is between minimum and maximum
                if left == -1 and right == -1:
                    # both child are None
                    self.currentMax = max(self.currentMax, 1)
                    return 1
                if left + right > -1:
                    # one child is None and the other one is >= 1
                    self.currentMax = max(self.currentMax, left + right + 2)
                    # -1 + (left or right) + 1 + root
                    return left + right + 2
            if left > 0 and right > 0:
                # both child are not None and between minimum and maximum
                self.currentMax = max(self.currentMax, left + right + 1)
                return left + right + 1
            return 0
        else:
            return -1


node1 = TreeNode(7)
node2 = TreeNode(3)
node3 = TreeNode(10)
node4 = TreeNode(2)
node5 = TreeNode(4)
node6 = TreeNode(8)
node7 = TreeNode(11)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7

test = Solution()
print test.maxSubtree(node1, 2, 12)
