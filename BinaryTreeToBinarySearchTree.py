# 1) Create a temp array arr[] that stores inorder traversal of the tree. This step takes O(n) time.
# 2) Sort the temp array arr[]. Time complexity of this step depends upon the sorting algorithm. In the following implementation, Quick Sort is used which takes (n^2) time. This can be done in O(nLogn) time using Heap Sort or Merge Sort.
# 3) Again do inorder traversal of tree and copy array elements to tree nodes one by one. This step takes *O(n) time.  (*Not really, nodes.pop(0) also takes time)

def binaryTreeToBST(root):
    if not root:
        return None
    nodes = []
    storePreOrder(root, nodes)
    nodes.sort()
    buildBST(root, nodes)


def storePreOrder(root, nodes):
    if not root:
        return
    storePreOrder(root.left, nodes)
    nodes.append(root.val)
    storePreOrder(root.right, nodes)

def buildBST(root, nodes):
    if not root:
        return
    buildBST(root.left, nodes)
    root.val = nodes.pop(0)
    buildBST(root.right, nodes)