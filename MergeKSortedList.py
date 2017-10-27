# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# use self-implemented heapsort (priority queue)
# Time complexity is O(NlogK), N is total nodes number, K is list number
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # use min heap
        head = cur = ListNode(None)
        # remove None obj in lists
        arry = []
        for node in lists:
            if node:
                arry.append(node)
        self.buildHeap(arry) # O(K), buildHeap is linear time
        while arry: # O(N)
            node = arry[0]
            cur.next = node
            cur = cur.next
            if node.next:
                arry[0] = node.next
            else:
                # switch first and last element, make pop() quick
                arry[0], arry[-1] = arry[-1], arry[0]
                arry.pop()
            self.heapify(arry, 0)   # heapify is O(logK)
        return head.next

    def buildHeap(self, arry):
        for i in range(len(arry)/2-1, -1, -1):
            self.heapify(arry, i)

    def heapify(self, arry, root):
        """
        root: the position that needs heapify
        """
        length = len(arry)
        # the index of left child is 2*root+1, right child is 2*root+2
        left_child = 2 * root + 1
        right_child = 2 * root +2
        # right_child is in the arry
        if right_child <= length - 1:
            if arry[left_child].val < arry[right_child].val:
                min_child = left_child
            else:
                min_child = right_child
            if arry[min_child].val < arry[root].val:
                arry[root], arry[min_child] = arry[min_child], arry[root]
                self.heapify(arry, min_child)
        # right_child is not, left_child is in the arry
        elif left_child <=  length -1 :
            if arry[left_child].val < arry[root].val:
                arry[root], arry[left_child] = arry[left_child], arry[root]
                # self.heapify(arry[left_child])  # not necessary


# use heapq
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
            if node[1].next:
                heappush(array, (node[1].next.val, node[1].next))
        return res.next

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)
node1.next = node5
node2.next = node4
node3.next = node6

lists=[node1, node2, node3]

test = Solution()
cur = test.mergeKLists(lists)
while cur:
    print cur.val
    cur = cur.next