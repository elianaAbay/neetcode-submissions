class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #so out list should not contain any duplicated. 
        #-> [], [[]]
        #using a set, out memory complecity ->o(n), n being the subset we've created 
        # [], [1], [1,2], [1,3], [2], [2, 3], [3], [1,2,3], time complecity o(n^2)

        res = []
        subset = []
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return 

            
            #the decision to include num[i]
            subset.append(nums[i])
            dfs(i+1)

            #decision not to include nums[i]
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res 


            