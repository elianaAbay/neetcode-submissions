class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        stack = []

        res = []

        def backtrack(openC, closed):
            if openC == closed == n:
                res.append("".join(stack))
                return
                
            if openC < n:
                stack.append("(")
                backtrack(openC + 1, closed)
                stack.pop()
            
            if closed < openC:
                stack.append(")")
                backtrack(openC , closed + 1)
                stack.pop()

        backtrack(0, 0)
        return res


