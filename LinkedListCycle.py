# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        oneStep = head
        if not oneStep:
            return False
        twoStep = oneStep.next
        while not oneStep is twoStep:
            if twoStep:
                nextOne = twoStep.next
                if not nextOne:
                    return False
                twoStep = nextOne.next
                oneStep = oneStep.next
            else:
                return False
        return True

# Using Exception
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        try:
            oneStep = head
            twoStep = head.next.next
            while not oneStep is twoStep:
                oneStep = oneStep.next
                twoStep = twoStep.next.next
            return True
        except:
            return False

