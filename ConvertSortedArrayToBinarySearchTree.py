# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        # helper function is used to return the entire sub tree structure
        return self.helper(nums)
    
    def helper(self, nums):
        if not nums:
            return None
        else:            
            mid = len(nums)/2
            root = TreeNode(nums[mid])
            if len(nums) > 1:
                root.left = self.helper(nums[:mid])
                root.right = self.helper(nums[mid+1:])
            return root

test = Solution()
root = test.sortedArrayToBST([1,2,3,4])
print root.val, root.left.val, root.right.val

