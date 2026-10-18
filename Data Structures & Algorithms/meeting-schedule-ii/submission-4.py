"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        count = 0
        res = 0
        i = 0
        j = 0
        while i < len(start) or j < len(end):
            if i< len(start) and start[i] < end[j]:
                count += 1
                i += 1
            elif j < len(end):
                count -= 1
                j += 1
            res = max(res, count)
        
        return res

        