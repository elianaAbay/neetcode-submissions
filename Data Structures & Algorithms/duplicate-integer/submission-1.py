from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = Counter(nums)
        print(count)

        for value in count.values():
            if value > 1:
                return True 
            
        return False 