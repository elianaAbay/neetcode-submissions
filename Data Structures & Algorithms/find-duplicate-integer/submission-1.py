class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0 
        fast = 1

        nums.sort()
        while slow < fast and nums[slow] != nums[fast]:
            slow = slow + 1 
            fast = fast + 1 

        return nums[slow]






