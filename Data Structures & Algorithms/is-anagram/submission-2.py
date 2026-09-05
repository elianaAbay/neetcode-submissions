from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = "".join(sorted(s))
        t = "".join(sorted(t))
        
        i = 0

        if len(s) != len(t):
            return False

        while i < len(s):
            if t[i] != s[i]:
                return False 
            i += 1
        
        return True
            