class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0])


        merge = [intervals[0]]
        for start, end in intervals:
            pop = merge[-1]
            
            if pop[1] >= start:
                pop[1] = max(pop[1], end)

            else:
                merge.append([start, end])

        return merge
