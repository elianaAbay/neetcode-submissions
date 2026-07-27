class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res= []
        lst = []
        seen = set()

        def backtrack():
            if len(lst) == len(nums):
                res.append(lst.copy())
                return 
            
            for num in nums:
                if num in seen:
                    continue 
                
                lst.append(num)
                seen.add(num)
                backtrack()
                lst.pop()
                backtrack()
                seen.remove(num)

        backtrack()
        return res
                