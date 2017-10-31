class Solution(object):
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        # use fractions to store numerators and denomenator with sign on numer
        # fraction = [(numer, denom)]
        fractions = []
        sign = 1
        start = 0
        for i, ch in enumerate(expression):
            if ch == '+' or ch == '-':
                fraction = expression[start:i]
                if fraction:
                    fractions.append((sign*int(fraction.split('/')[0]), int(fraction.split('/')[1])))
                if ch == '+':
                    sign = 1
                else:
                    sign = -1
                start = i + 1
        fraction = expression[start:]
        fractions.append((sign*int(fraction.split('/')[0]), int(fraction.split('/')[1])))
        # print fractions
        subtotal = (0,1)
        for fraction in fractions:
            subtotal = self.add(subtotal, fraction)
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