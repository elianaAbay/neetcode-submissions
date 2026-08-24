from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        d = Counter(s)
        t = Counter(t)

      
     

        return d == t
        