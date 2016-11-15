# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x=1):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.maximum = 1
    def maxDepth(self, root): 
        if root == None:
            return 0
        self.findchild(root, 1)
        return self.maximum
    def findchild(self, node, depth):
        if node.left:
            if self.maximum < depth + 1:
                self.maximum = depth + 1
            self.findchild(node.left, depth+1)
        if node.right:
            if self.maximum < depth + 1:
                self.maximum = depth + 1
            self.findchild(node.right, depth+1)
class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def maxDepth(self, root):
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

node1 = TreeNode()
node2 = TreeNode()
node3 = TreeNode()
node4 = TreeNode()
node5 = TreeNode()
node6 = TreeNode()
node7 = TreeNode()
node8 = TreeNode()
node9 = TreeNode()

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7
node7.right = node8
node8.left = node9
test = Solution()
print node1.left
print test.maxDepth(node1)