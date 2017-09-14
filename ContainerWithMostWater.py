class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        start = 0
        end = len(height)-1
        volume = 0
        while start < end:
            volume = max(volume, (end-start)*min(height[start], height[end]))
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        return volume

test = Solution()
print test.maxArea([1,5,3,5,4])