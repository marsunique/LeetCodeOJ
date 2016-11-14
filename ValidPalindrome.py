class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == '':
            return True
        head = 0
        tail = len(s)-1
        while head < tail:
            if s[head].isalnum() and s[tail].isalnum():
                if s[head].lower() != s[tail].lower():
                    return False
                head += 1
                tail -= 1
            elif not s[head].isalnum():
                head += 1
            elif not s[tail].isalnum():
                tail -= 1
        return True
        
        
test = Solution()
print test.isPalindrome(',.')