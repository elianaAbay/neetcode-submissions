class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []
        def backtrack(indx, total, lst):
            if indx >= len(nums) or total > target:
                return 

            if total == target:
                res.append(lst.copy())
                return 

            lst.append(nums[indx])
            backtrack(indx, total + nums[indx], lst)
            lst.pop()
            backtrack(indx + 1 , total,lst)
        
        backtrack(0, 0 , [])
        return res
        

        

