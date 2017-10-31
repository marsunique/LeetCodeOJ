class Solution(object):
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        # use fraction to store numerators and denomenator with sign on numer
        # fraction = (numer, denom)
        sign = 1
        start = 0
        subtotal = (0,1)
        for i, ch in enumerate(expression):
            if ch == '+' or ch == '-':
                fraction = expression[start:i]
                if fraction:
                    subtotal = self.add(subtotal, (sign*int(fraction.split('/')[0]), int(fraction.split('/')[1])))
                if ch == '+':
                    sign = 1
                else:
                    sign = -1
                start = i + 1
        fraction = expression[start:]
        subtotal = self.add(subtotal, (sign*int(fraction.split('/')[0]), int(fraction.split('/')[1])))
        gcd = self.gcd(subtotal[0], subtotal[1])
        return str(subtotal[0]/gcd) + '/' + str(subtotal[1]/gcd)
        
    def add(self, f1, f2):
        numer = f1[0]*f2[1] + f1[1]*f2[0]
        denom = f1[1]*f2[1]
        return (numer, denom)

    def gcd(self, a, b):
        if not a % b:
            return b
        else:
            return self.gcd(b, a%b)

test = Solution()
print test.fractionAddition('-1/2+1/2+1/3')
print test.gcd(18, 42)