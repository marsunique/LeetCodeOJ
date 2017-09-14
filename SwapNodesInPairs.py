# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        real_head = ListNode(0)
        real_head.next = head
        if not real_head.next or not real_head.next.next:
            return real_head.next
        prior_one = real_head
        node1 = real_head.next
        node2 = real_head.next.next
        while node1 and node2:
            # switch
            next_one = node2.next
            node2.next = node1
            node1.next = next_one
            prior_one.next = node2
            # update
            prior_one = node1
            node1 = next_one
            if not next_one:
                return real_head.next
            node2 = next_one.next
        return real_head.next

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node1.next = node2
node2.next = node3
test = Solution()
head = test.swapPairs(node1)
while head:
    print head.val
    head = head.next