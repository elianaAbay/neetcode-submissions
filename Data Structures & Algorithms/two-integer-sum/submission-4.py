class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #[3,4,5,6], target = 7

        diff_map = {}

        i = 0

        for n in (nums):
            diff = target - n 

            if diff in diff_map:
                return [diff_map[diff],i]

            diff_map[n] = i
            i+=1
