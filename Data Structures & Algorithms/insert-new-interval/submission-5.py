class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        l, r = 0, len(intervals) -1 

        while l <= r:
            mid = (l + r ) // 2

            #
            if intervals[mid][0] <= newInterval[0]:
                l = mid + 1
            
            else:
                r = mid -1

        intervals.insert(l, newInterval)

        print(intervals)

        
        merg = [intervals[0]]

        for start, end in intervals:
            pop = merg[-1]

            if pop[1] >= start:
                pop[1] = max(pop[1], end)
            else:
                merg.append([start, end])
            
        
        return merg