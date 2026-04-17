class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        found = set(nums)

        maxfound = 0
        for num in found:
            if num - 1 not in nums:
                count = 1 

                while num + count in nums:
                    count += 1
                
                maxfound = max(maxfound, count)

        return maxfound

        


        