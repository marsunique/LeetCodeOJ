class Solution(object):
    def longestPhrase(self, a, k):
        """
        :type a: List[int]
        :type k: int
        """
        remain = k
        head = 0
        tail = 0
        # two pointers indicate the start and end position
        max_len = 0
        while tail < len(a):
            if remain < a[tail]:    # no enough room for a[tail]
                if head == tail:        # head and tail are at same pos
                    head += 1
                    tail += 1
                else:                   # head is before tail
                    max_len = max(max_len, tail - head)
                    remain += a[head]
                    head += 1
            else:
                remain -= a[tail]
                tail += 1
        max_len = max(max_len, tail - head)
        return max_len

test = Solution()
print test.longestPhrase([5,8,1,2,3], 6)
