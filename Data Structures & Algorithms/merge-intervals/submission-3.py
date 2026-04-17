class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0])

        lst = [intervals[0]]

        for start, end in intervals[1:]:
            pop = lst[-1]
            if pop[1] >= start:
                pop[1] = max(pop[1], end)
            else:
                lst.append([start, end])

        return lst
