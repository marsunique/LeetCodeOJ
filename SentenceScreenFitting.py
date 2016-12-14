# class Solution(object):
#     def wordsTyping(self, sentence, rows, cols):
#         """
#         :type sentence: List[str]
#         :type rows: int
#         :type cols: int
#         :rtype: int
#         """
#         words_len = [len(word) for word in sentence]
#         self.sentence_len = len(sentence) 
#         self.count = 0
#         index = 0
#         for i in range(rows):
#             start_position = 1
#             while start_position <= cols:
#                 end_position = start_position + words_len[index] - 1
#                 if end_position <= cols:
#                     index = self.indexIncrease(index)
#                     start_position = end_position + 2
#                 else:
#                     break
#         return self.count
#     def indexIncrease(self, index):
#         if index == self.sentence_len - 1:
#             self.count += 1
#             return 0
#         else:
#             return index+1


# class Solution(object):
#     def wordsTyping(self, sentence, rows, cols):
#         """
#         :type sentence: List[str]
#         :type rows: int
#         :type cols: int
#         :rtype: int
#         """
#         words_len = [len(word) for word in sentence]
#         for word_len in words_len:
#             if word_len > cols:
#                 return 0
#         word_count = 0
#         index = 0
#         start_position = 0
#         while start_position <= rows*cols-1:
#             end_position = start_position + words_len[index] - 1
#             if start_position/cols == end_position/cols:
#                 # print sentence[index]
#                 # print 'start', start_position
#                 # print 'end', end_position
#                 word_count += 1
#                 index = (index + 1) % len(sentence)
#                 if end_position % cols == cols - 1:
#                     start_position = end_position + 1
#                 else:
#                     start_position = end_position + 2
#             else:
#                 start_position = (end_position / cols) * cols + 1
#         return word_count/len(sentence)

class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        s = " ".join(sentence) + " "
        print s
        start, n = 0, len(s)
        for i in range(0, rows):
            print 'before', start
            start += cols
            print 'after', start
            if s[start % n] == " ":
                start += 1
            else:
                while start > 0 and s[(start-1) % n] != " ":
                    start -= 1
        return start / n
test = Solution()
print test.wordsTyping(["abc", "de", "f"], 4, 6)