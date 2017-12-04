class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        elements = self.helper(formula)
        res = ''
        for key in sorted(elements.keys()):
            if elements[key] == 1:
                res = res + key
            else:
                res = res + key + str(elements[key])
        return res

    def helper(self, formula):
        elements = {}
        if not formula:
            return elements
        i = 0
        while i < len(formula):
            # parenthesis, use recursion
            if (formula[i] == '('):
                # find the end of paired parenthesis
                flag = 0
                for j in range(i, len(formula)):
                    if formula[j] == '(':
                        flag += 1
                    if formula[j] == ')':
                        flag -= 1
                    if flag == 0:
                        break
                # recursion
                partial_elements = self.helper(formula[i+1:j])

                # get the number after ')'
                num = 1
                k = j+1
                while k < len(formula) and formula[k].isdigit():
                    k += 1
                if k > j+1:
                    num = int(formula[j+1:k])

                # add partial_elements to elements
                for key in partial_elements:
                    elements[key] = elements.get(key, 0) + (partial_elements[key] * num)
                i = k

            else:
                j = i+1
                while j < len(formula) and formula[j].islower():
                    j += 1

                # get the number after element
                num = 1
                k = j
                while k < len(formula) and formula[k].isdigit():
                    k += 1
                if k > j:
                    num = int(formula[j:k])
                key = formula[i:j]
                elements[key] = elements.get(key, 0) + num
                
                i = k
        return elements


test = Solution()
print test.countOfAtoms('Mg(OH)2')