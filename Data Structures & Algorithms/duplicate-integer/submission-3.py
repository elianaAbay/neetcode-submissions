class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        val = set()
        
        for i in nums:
            val.add(i)

        if len(val) == len(nums):
            return False
        else:
            return True

        