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
        real_head = ListNode(-1)
        real_head.next = head
        p = real_head.next
        while p:
            if p is real_head.next:
                temp = p.next
                p.next = None
                p = temp
                # if p is the first node, p.next = None
            else:
                temp = real_head.next
                real_head.next = p
                temp2 = p.next
                p.next = temp
                p = temp2
                # if p is not the first node, insert p behind head
        return real_head.next
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