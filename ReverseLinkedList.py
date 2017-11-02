# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        cur = head.next
        head.next = None    # avoid infinite loop
        while cur:
            temp = cur.next
            cur.next = head
            head = cur
            cur = temp
        return head
# Recursive
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        else:
            new_head = self.reverseList(head.next)
            head.next.next = head
            head.next = None
            return new_head

node1 = ListNode(1)
node2 = ListNode(2)
node1.next = node2
test = Solution()
head = test.reverseList(node1)
while head:
    print head.val
    head = head.next