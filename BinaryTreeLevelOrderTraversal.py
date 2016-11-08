# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
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
            # queue = [[node1.left, node1.right], [node2.left, node2.right]]
            print 'queue',queue
            temp = [child.val for pair in queue for child in pair if child]
            print 'temp',temp
            if len(temp):
                res.append(temp)
            print 'res',res
        return res

node1 = TreeNode(3)
node2 = TreeNode(9)
node3 = TreeNode(20)
node4 = TreeNode(15)
node5 = TreeNode(7)

node1.left = node2
node1.right = node3
node3.left = node4
node3.right = node5

test = Solution()
print test.levelOrder(node1)