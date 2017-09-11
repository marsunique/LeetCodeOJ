import re

class Solution(object):
    def mask(self, s):
        """
        :type s: str
        """
        s = s.strip()
        content = s.split(':')[1].strip().replace(' ', '')  # remove spaces
        if s[0] == 'E':
            return self.maskEmail(content)
        else:
            return self.maskPhone(content)

    def maskEmail(self, email):
        username = email.split('@')[0]
        domain = email.split('@')[1]
        return username[0] + '*****' + username[-1] + '@' + domain

    def maskPhone(self, phone):
        phone = re.sub('[\+\-()]', '', phone)   # use regex to remove chars, '+' and '-'
        length = len(phone)                     # have special meanings in regex, need escape
        if length > 10:
            return '+' + '*' * (length-10) + '-***-***-' + phone[-4:]
        else:
            return '***-***-' + phone[-4:]


test = Solution()
print test.mask('E:google@gmail.com')
print test.mask('P:+1(001)123-4567')