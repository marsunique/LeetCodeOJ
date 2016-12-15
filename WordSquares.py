class Solution(object):
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        n = len(words[0])
        if n == 1:
            return [words]
        self.prefixCollection = {}
        self.squares = []
        for word in words:
            for i in range(n):
                self.prefixCollection.setdefault(word[:i],[])
                self.prefixCollection[word[:i]].append(word)
        # print self.prefixCollection
        
        for word in words:
            square = []
            square.append(word)
            self.build(square, 1, n)
        return self.squares

    def build(self, square, row, n):
        # calculate the prefix of current square
        prefix = ''
        for i in range(0, row):
            prefix += square[i][row]
        
        if prefix in self.prefixCollection:
            bag = self.prefixCollection[prefix]
            for word in bag:
                new_square = square[:]
                # !! can only use slice, cannot use new_square = square, it refers to the same object and will change square
                new_square.append(word)
                if len(new_square) == n:
                    self.squares.append(new_square)
                else:
                    self.build(new_square, row+1, n)

test = Solution()
print test.wordSquares(["abat","baba","atan","atal"])