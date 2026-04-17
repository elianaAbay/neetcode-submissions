class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #two dictionaries, one for s and one for t 
        if len(s) != len(t):
            return False
            
        dict1 = {}
        dict2 = {}

        for num in s:
            if num not in dict1:
                dict1[num] = 1
            else:
                dict1[num] += 1
        
        for num in t:
            if num not in dict2:
                dict2[num] = 1
            else:
                dict2[num] += 1

        for i  in dict1:
            if i not in dict2 or dict2[i] != dict1[i]:
                return False

        return True 

        

            
        
