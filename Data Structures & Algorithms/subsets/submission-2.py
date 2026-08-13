class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtrack(i, lst):
            if i > len(nums):
                return

            if i == len(nums):
                res.append(lst.copy())
                return 
            

            lst.append(nums[i])
            backtrack(i + 1, lst)
            lst.pop()
            backtrack(i+ 1, lst)
        
        backtrack(0, [])
        return res