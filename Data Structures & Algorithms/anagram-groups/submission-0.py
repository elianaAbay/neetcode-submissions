class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        d = {}
        for i in strs:
            j = "".join(sorted(i))

            if j  in d:
                d[j].append(i)
            else:
                d[j] = [i]

        res = list(d.values())
        return res
     
            
        