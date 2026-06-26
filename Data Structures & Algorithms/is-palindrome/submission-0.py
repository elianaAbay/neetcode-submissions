class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.strip()
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        s = s.lower()

        left, right = 0, len(s) - 1

        while left <= right:
            if s[left] != s[right]:
                return False

            right -= 1
            left += 1
        return True