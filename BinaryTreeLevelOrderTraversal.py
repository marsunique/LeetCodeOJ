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
            return []
        nodes = [root]  # store nodes on current level
        while nodes:
            temp_nodes = [] # store nodes from next level
            vals = []   # store value of nodes from current level
            for node in nodes:
                vals.append(node.val)
                if node.left:
                    temp_nodes.append(node.left)
                if node.right:
                    temp_nodes.append(node.right)
            res.append(vals)
            nodes = temp_nodes
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