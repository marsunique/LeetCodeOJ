class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        for row in matrix:
            for col in range(1, len(row)):
                row[col] = row[col-1] + row[col]
        self.matrix = matrix
        print self.matrix

    def update(self, row, col, val):
        """
        update the element at matrix[row,col] to val.
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        if col:
            diff = val - (self.matrix[row][col]-self.matrix[row][col-1])
        else:
            diff = val - self.matrix[row][col]
        for i in range(col, len(self.matrix[row])):
            self.matrix[row][i] += diff

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        sum = 0
        for row in range(row1, row2+1):
            sum += self.matrix[row][col2]
            if col1:
                sum -= self.matrix[row][col1-1]
        return sum

matrix = [[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]
# Your NumMatrix object will be instantiated and called as such:
numMatrix = NumMatrix(matrix)
print numMatrix.sumRegion(2, 1, 4, 3)
numMatrix.update(3, 2, 2)
print numMatrix.sumRegion(2, 1, 4, 3)