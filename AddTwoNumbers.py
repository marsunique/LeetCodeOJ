# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        head = ListNode(-1)
        cur = head
        while l1 or l2 or carry:
            sum = carry
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            carry = sum/10
            sum = sum%10
            node = ListNode(sum)
            cur.next = node
            cur = cur.next
        return head.next

# in-place, no extra link list
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(-1)
        head.next = l1
        pre = head
        carry = 0
        while l1 and l2:
            sum = l1.val + l2.val + carry
            l1.val = sum % 10
            carry = sum / 10
            pre = l1
            l1 = l1.next
            l2 = l2.next
        while l1:
            sum = l1.val + carry
            l1.val = sum % 10
            carry = sum / 10
            if not carry:
                break
            pre = l1
            l1 = l1.next
        while l2:
            pre.next = l2
            sum = l2.val + carry
            l2.val = sum % 10
            carry = sum / 10
            if not carry:
                break
            pre = pre.next
            l2 = l2.next
        if carry == 1:
            node = ListNode(1)
            pre.next = node
        return head.next