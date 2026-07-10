import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-n for n in stones] 
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            x = heapq.heappop(max_heap)
            y = heapq.heappop(max_heap)

            if abs(x) == abs(y):
                continue 
            
            elif abs(x) > abs(y):
                newVal = x - y
                heapq.heappush(max_heap, newVal)
        

        if len(max_heap) == 0:
            return 0 
        else:
            return abs(max_heap[0])