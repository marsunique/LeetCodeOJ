class OA1(object):
    def run(self, s, k):
        length = len(s)
        count = 0
        res = ''
        for i in range(length-1, -1, -1):
            if s[i] == '-':
                continue
            else:
                if count < k:
                    res = s[i].upper() + res
                    count += 1
                else:
                    res = s[i].upper() + '-' + res
                    count = 1
        return res
    def run2(self, s, k):
        length = len(s)
        count = 0
        res = ''
        for i in range(length-1, -1, -1):
            if s[i] == '-':
                continue
            else:
                if count < k:
                    if s[i].isalpha():
                        res = s[i].upper() + res
                    else:
                        res = s[i] + res
                    count += 1
                else:
                    if s[i].isalpha():
                        res = s[i].upper() + '-' + res
                    else:
                        res = s[i] + '-' + res
                    count = 1
        return res
test = OA1()
print test.run('-aa213aa---Z', 4)
print test.run2('z', 1)
