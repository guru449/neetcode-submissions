"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        intervals.sort(key = lambda x: x.start)
    
        beginTimes = [0] * len(intervals)
        endTimes = [0] * len(intervals)

        for i  in range(len(intervals)):
            beginTimes[i] = intervals[i].start
            endTimes[i] = intervals[i].end
        beginTimes.sort()
        endTimes.sort()
        i = 0
        j = 0

        rooms = 0
        result = 0
        while i < len(beginTimes):
            if beginTimes[i] < endTimes[j]:
                rooms += 1
                result = max(result, rooms)
                i += 1
            else:
                rooms -= 1
                j += 1
        return result


        