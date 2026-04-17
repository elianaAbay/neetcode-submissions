class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        candidates.sort()
        

        def backtrack(i, cur, t):
            if t == target:
                res.append(cur.copy())
                return 
            
            if i >= len(candidates) or t > target:
                return 


            cur.append(candidates[i])
            backtrack(i + 1, cur, t + candidates[i])

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            
            cur.pop()
            backtrack(i + 1, cur, t)

        backtrack(0, [], 0)

        return res
        