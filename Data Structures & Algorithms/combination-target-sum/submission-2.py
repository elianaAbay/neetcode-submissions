class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []

        def backtrack(i, cur, t):
            if t == target:
                res.append(cur.copy())
                return 

            if i >= len(nums) or t > target:
                return     

            
            cur.append(nums[i])
            backtrack(i, cur, t + nums[i])

            cur.pop()
            backtrack(i + 1 , cur, t)
        
        backtrack(0, [], 0)
        return res


