class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # use set, if the length remains the same, there is no duplicates.
        # refer to https://discuss.leetcode.com/topic/20016/1-7-lines-python-4-solutions/3
        existed = []
        for row, row_content in enumerate(board):
            for col, ele in enumerate(row_content):
                if ele != '.':
                    existed += [(row, ele), (ele, col), (row/3, col/3, ele)]
        if len(set(existed)) == len(existed):
            return True
        return False

board = [
    ['.','.','.','.','.','.','.','.','.'],
    ['.','2','.','.','.','.','.','.','.'],
    ['.','.','1','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.','.']
]
test = Solution()
print test.isValidSudoku(board)