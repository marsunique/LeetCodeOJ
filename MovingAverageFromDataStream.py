class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.n = size
        self.window = []
        self.preAverage = 0

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        curLen = len(self.window)
        if curLen == self.n:
            preNumber = self.window.pop(0)
            self.window.append(val)
            print self.window
            self.preAverage = (float(val - preNumber) / self.n + self.preAverage)
        else:
            self.window.append(val)
            self.preAverage = float(self.preAverage * curLen + val) / (curLen + 1)

        return self.preAverage

# Your MovingAverage object will be instantiated and called as such:
obj = MovingAverage(3)
print obj.next(1)
print obj.next(4)
print obj.next(9)
print obj.next(10)
print obj.next(1)