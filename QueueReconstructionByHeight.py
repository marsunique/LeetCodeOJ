class Solution(object):
    def reconstructQueue(self, people):
        people_dict = {}
        height = []
        result = []
        for each_person in people:
            if each_person[0] in people_dict:
                people_dict[each_person[0]].append((each_person[1], each_person))
            else:
                people_dict[each_person[0]] = [(each_person[1], each_person)]
                height.append(each_person[0])
            #print people_dict
        height.sort()
        height = height[::-1]
        #print height
        for each_height in height:
            people_with_height = people_dict[each_height]
            people_with_height.sort()
            for each_person in people_with_height:
                result.insert(each_person[0],each_person[1])
        return result

array = [[7,2], [5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
s = Solution()
res = s.reconstructQueue(array)
print res