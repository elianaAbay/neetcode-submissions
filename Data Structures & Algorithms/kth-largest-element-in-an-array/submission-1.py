import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #[1,2,3,4,5]

        max_heap = [-n for n in nums]
        heapq.heapify(max_heap)
        print(max_heap)  

        i = 1
        while i < k:
            heapq.heappop(max_heap)
            i += 1

        x = heapq.heappop(max_heap)
        return -x