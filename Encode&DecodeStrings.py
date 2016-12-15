class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        res = ''
        for s in strs:
            res = res + str(len(s)) + '|' + s
        return res

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        res = []
        word = ''
        i = 0
        length = ''
        while i < len(s):
            if s[i] == '|':
                next_position = i + int(length) + 1
                word = s[i+1:next_position]
                res.append(word)
                i = next_position
                length = ''
            else:
                length += s[i]
                i += 1
        return res