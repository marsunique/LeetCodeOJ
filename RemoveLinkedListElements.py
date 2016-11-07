# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        head_node = ListNode(-1)
        head_node.next = head
        node = head_node
        while node.next!= None:
            if node.next.val == val:
                node.next = node.next.next
            else:
                node = node.next
        return head_node.next

node1 = ListNode(1)
node2 = ListNode(1)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(1)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

test = Solution()
head = test.removeElements(node1,1)
while head:
    print head.val
    head = head.next