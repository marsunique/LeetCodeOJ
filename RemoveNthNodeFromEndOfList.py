# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        slow = head
        fast = head
        for i in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast:
            prior = slow
            slow = slow.next
            fast = fast.next
        prior.next = prior.next.next
        return head
            

