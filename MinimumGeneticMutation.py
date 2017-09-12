class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        if not end in bank:
            return -1
        queue = [(start, 0)]
        while queue:
            cur_gene, count = queue.pop(0)
            if cur_gene == end:
                return count
            else:
                for gene in bank:
                    if self.validMutation(cur_gene, gene):
                        queue.append((gene, count+1))
        return -1            


    def validMutation(self, cur_gene, gene):
        num_change = 0
        for i in range(len(gene)):
            if cur_gene[i] != gene[i]:
                num_change += 1
        return num_change == 1

start = 'AACCGGTT'
end = 'AACCGGTA'
bank = ['AACCGGTA']
test = Solution()
print test.minMutation(start, end, bank)