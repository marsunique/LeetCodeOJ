# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Preorder
def preorder(root):
    res = []
    stack = []
    while stack or root:
        if root:
            res.append(root.val)
            stack.append(root)
            root = root.left
        else:
            node = stack.pop()
            root = node.right
    return res
# Inorder
def inorder(root):
    res = []
    stack = []
    while stack or root:
        if root:
            stack.append(root)
            root = root.left
        else:
            node = stack.pop()
            res.append(node.val)
            root = node.right
    return res
# Postorder
def postorder(root):
    res = []
    if not root:
        return res
    pre = None
    stack = [root]
    while stack:
        top = stack[-1]
        # If stack top node has no child or its children have 
        # been looked up, then it can be poped and looked up
        if (not top.left and not top.right) or (pre is top.left or pre is top.right):
            res.append(top.val)
            pre = stack.pop()
        else:
            if top.right:
                stack.append(top.right)
            if top.left:
                stack.append(top.left)
    return res
    # # Another approach to postorder traversal, tricky one
    # # root->right->left and reverse the result
    # res = []
    # stack = []
    # while stack or root:
    #     if root:
    #         res.append(root.val)
    #         stack.append(root)
    #         root = root.right
    #     else:
    #         node = stack.pop()
    #         root = node.left
    # return res[::-1]

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

print preorder(node1)
print inorder(node1)
print postorder(node1)