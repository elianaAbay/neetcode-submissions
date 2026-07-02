class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset =[]
        perm = []

        def backtrack(i):
            if i == len(nums):
                subset.append(perm.copy())
                return 
            
            perm.append(nums[i])
            backtrack(i + 1)
            perm.pop()
            backtrack(i+1)
        
        backtrack(0)
        return subset