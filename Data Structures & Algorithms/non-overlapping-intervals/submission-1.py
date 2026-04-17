class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[0])

        count = 0 

        merged = [intervals[0]] #1,2  1,2 1, 4, 2, 4
        for start, end in intervals:

            if start < merged[-1][1]:
                count += 1
                merged[-1][1] = min(merged[-1][1], end)

            else:
                merged.append([start, end])

            

        return count -1
        
