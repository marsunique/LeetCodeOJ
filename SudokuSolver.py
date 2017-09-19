class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        row_dic = {}    #{(row_num, ele):1, ...}
        col_dic = {}    #{(ele, col_num):1, ...}
        square_dic = {} #{(row/3, col/3, ele):1, ...}
        for row, row_content in enumerate(board):
            for col, ele in enumerate(row_content):
                if ele != '.':
                    row_dic.setdefault((row, ele), 1)
                    col_dic.setdefault((ele, col), 1)
                    square_dic.setdefault((row/3, col/3, ele), 1)
        self.solve(row_dic, col_dic, square_dic, board)
        print board

    def solve(self, row_dic, col_dic, square_dic, board):
        # check if all blank is filled
        # if True, return true
        complete = True
        for row in board:
            if '.' in row:
                complete = False
        if complete:
            return True

        for row, row_content in enumerate(board):
            for col, ele in enumerate(row_content):
                if ele == '.':
                    for num in range(1,10):
                        str_num = str(num)
                        if (not (row, str_num) in row_dic) and (not (str_num, col) in col_dic) and (not (row/3, col/3, str_num) in square_dic):
                            board[row][col] = str_num
                            row_dic.setdefault((row, str_num), 1)
                            col_dic.setdefault((str_num, col), 1)
                            square_dic.setdefault((row/3, col/3, str_num), 1)
                            # try to fill next blank until no blank left
                            if self.solve(row_dic, col_dic, square_dic, board):
                                return True
                            else:
                                # fail to fill future blanks, revert
                                board[row][col] = '.'
                                del(row_dic[(row, str_num)])
                                del(col_dic[(str_num, col)])
                                del(square_dic[(row/3, col/3, str_num)])
                    # filling current blank fail
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
test.solveSudoku(board)
