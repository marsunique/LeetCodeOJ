class ValidWordAbbr(object):
    def __init__(self, dictionary):
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        self.dict = {}
        for s in dictionary:
            if len(s) < 3:
                abbr = s
            else:
                abbr = s[0] + str(len(s)-2) + s[-1]
            self.dict.setdefault(abbr, [])
            if not s in self.dict[abbr]:
                self.dict[abbr].append(s)
        

    def isUnique(self, word):
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        if len(word) < 3:
            abbr = word
        else:
            abbr = word[0] + str(len(word)-2) + word[-1]
        if abbr in self.dict:
            if word in self.dict[abbr] and len(self.dict[abbr]) > 1:
                return False
            elif not word in self.dict[abbr]:
                return False
        return True
        


# Your ValidWordAbbr object will be instantiated and called as such:
vwa = ValidWordAbbr(["deer", "door", "cake", "card"])
# vwa.isUnique("word")
# vwa.isUnique("anotherWord")