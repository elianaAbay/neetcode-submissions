class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans, sol = [], []

        def backtrack(openN, close):
            if openN == close == n:
                ans.append("".join(sol))
                return 
            
            if openN <n:
                sol.append("(")
                backtrack(openN + 1, close)
                sol.pop()
            
            if close < openN:
                sol.append(")")
                backtrack(openN, close+1)
                sol.pop()

        backtrack(0,0)
        return ans
            
            


