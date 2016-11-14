# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        from heapq import heapify, heappush, heappop, heapreplace
        res = cur = ListNode(-1)
        # res used to point the start position, cur used to create list
        array = [(node.val, node) for node in lists if node]
        heapify(array)
        while array:
            node = heappop(array)
            cur.next = node[1]
            cur = cur.next
            if not (node[1].next is None):
                heappush(array, (node[1].next.val, node[1].next))
        return res.next

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)

node1.next = node3
node2.next = node4

test = Solution()
res = test.mergeKLists([node1, node2])
while res:
    print res.val
    res = res.next