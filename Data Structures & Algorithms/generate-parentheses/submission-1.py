class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack (opening, closing, lst):
            if n == opening and n == closing:
                res.append("".join(lst.copy()))
                return 

            if opening < n:
                lst.append("(")
                backtrack(opening + 1, closing, lst)
                lst.pop()

            if closing < opening:
                lst.append(")")
                backtrack(opening, closing + 1, lst)
                lst.pop()
            
            
        backtrack(0,0,[])
        return res
