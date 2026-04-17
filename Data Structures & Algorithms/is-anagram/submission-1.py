class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
        dic2 = {}

        for j in t:
            if j not in dic2:
                dic2[j] = 1
            else:
                dic2[j] += 1
            
        for i in s:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
            
        return dic == dic2

    
    
        