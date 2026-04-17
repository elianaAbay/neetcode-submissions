class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key = lambda x:x[0])


        lst = [intervals[0]]
        count = 0 
        for start, end in intervals[1:]:
            pop = lst[-1]

            if pop[1] > start:
                count += 1
                pop[1] = min(pop[1], end)
            else:
                lst.append([start, end])

        print(lst)
        return count


        