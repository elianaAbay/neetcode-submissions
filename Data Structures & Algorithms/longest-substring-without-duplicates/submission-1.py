class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #abcabcbb abc xxx
        l, r = 0, 0
        hashset = set()
        res = 0

        while r < len(s):
            print(hashset)
            if s[r] not in hashset:
                hashset.add(s[r])
                r+=1
                res = max(res, len(hashset))
            
            else:
                hashset.remove(s[l])
                l+=1
                
        
        return res

            
                
