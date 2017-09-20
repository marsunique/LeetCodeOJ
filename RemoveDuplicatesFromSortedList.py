# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # ues two pointers, fast is one node ahead of slow
        # check fast.val ==? slow.val
        if not head:
            return head
        slow = head
        fast = head.next
        while fast:
            if fast.val == slow.val:
                slow.next = fast.next
                fast = fast.next
            else:
                slow = fast
                fast = fast.next
        return head