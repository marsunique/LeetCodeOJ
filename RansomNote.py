class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        dic = {}
        for letter in magazine:
            dic.setdefault(letter, 0)
            dic[letter] += 1
        for letter in ransomNote:
            dic.setdefault(letter, 0)
            dic[letter] -= 1
            if dic[letter] < 0:
                return False
        return True
        