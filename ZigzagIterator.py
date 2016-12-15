class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.vector = []
        for i in range(max(len(v1), len(v2))):
            for v in (v1 ,v2):
                if v:
                    self.vector.append(v.pop(0))
        print self.vector

    def next(self):
        """
        :rtype: int
        """
        if self.vector:
            return self.vector.pop(0)
        
    def hasNext(self):
        """
        :rtype: bool
        """
        return not self.vector == []

# Your ZigzagIterator object will be instantiated and called as such:
v1 = [1,2]
v2 = [3,4,5,6]
i, v = ZigzagIterator(v1, v2), []
while i.hasNext():
    v.append(i.next())
print v