class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        MAX = 0
        level_len={}
        lines = input.split('\n')
        for line in lines:
            length = len(line.lstrip('\t'))
            level = len(line) - length
            level_len[level] = length
            if '.' in line:
                temp = 0
                for i in range(0, level+1):
                    temp += level_len[i]
                MAX = max(MAX, temp+level)
        return MAX
test = Solution()
print test.lengthLongestPath("dir\n\t        file.txt\n\tfile2.txt")