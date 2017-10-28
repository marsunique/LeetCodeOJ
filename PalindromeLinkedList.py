# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True
        half_start = self.findHalfStart(head)
        # reverse the second half
        reversed_half_start = self.reverse(half_start)
        # check if first half equals to reversed second half
        cur_1 = head
        cur_2 = reversed_half_start
        # loop until cur_1 is half_start_node, means first half is end
        while not cur_1 is half_start:
            if cur_1.val != cur_2.val:
                return False
            cur_1, cur_2 = cur_1.next, cur_2.next
        return True
        
    def findHalfStart(self, head):
        slow = head
        fast = head
        while fast:
            if not fast.next:
                # means the number of nodes is odd
                return slow
            slow = slow.next
            fast = fast.next.next
        # means the number of nodes is even
        return slow

    def reverse(self, head):
        cur = head.next
        head.next = None    # avoid infinite loop
        while cur:
            temp = cur.next
            cur.next = head
            head = cur
            cur = temp
        return head

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(3)
node5 = ListNode(2)
node6 = ListNode(1)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

test = Solution()
print test.isPalindrome(node1)