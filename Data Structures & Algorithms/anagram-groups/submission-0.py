class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dic = {}

        for i in strs:
            key = "".join(sorted(i))
            if key not in dic:
                dic[key] = [i]
            else:
                dic[key].append(i)
        res = list(dic.values())
        return res