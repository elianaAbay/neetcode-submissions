"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        start = sorted([i. start for i in intervals])
        end = sorted([j.end for j in intervals])

        i, j  = 0, 0  
        count, res  = 0 , 0 

        while i < len(intervals):
            if start[i] < end[j]:
                i+= 1
                count += 1

            else:
                count -=1 
                j+= 1

            res = max(res, count)

        return res 

