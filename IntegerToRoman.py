class Solution(object):
    def charReplace(self, bit_value, digit):
        print bit_value
        print digit
        roman = {
            1 : 'I',
            2 : 'II',
            3 : 'III',
            4 : 'IV',
            5 : 'V',
            6 : 'VI',
            7 : 'VII',
            8 : 'VIII',
            9 : 'IX'
        }
        substitute = {
            'I' : ['I', 'X', 'C', 'M'],
            'V' : ['V', 'L', 'D', ''],
            'X' : ['X', 'C', 'M', ''],
        }
        return roman[bit_value].replace('X',substitute['X'][digit]).replace\
                                ('V',substitute['V'][digit]).replace('I',substitute['I'][digit])
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        res = ''
        digit_count = 0    # 0:unit, 1:decade, 2:hundreds, 3:kilo bit
        while num:
            bit_value = num % 10
            if bit_value != 0:
                res = self.charReplace(bit_value, digit_count) + res
            num = num / 10
            digit_count += 1
        return res

test = Solution()
print test.intToRoman(10)