class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = re.sub(r'[^a-zA-Z0-9]', '', s)
        
        s1 = s1.lower()
     
        return s1 == s1[::-1]
                