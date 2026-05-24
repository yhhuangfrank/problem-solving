"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = [i.start for i in intervals]
        end = [i.end for i in intervals]
        
        start.sort()
        end.sort()
        rooms, maxRooms = 0, 0
        i, j = 0, 0
        while i < len(intervals):
            if start[i] < end[j]:
                rooms += 1
                maxRooms = max(maxRooms, rooms)
                i += 1
            else:
                rooms -= 1
                j += 1
        return maxRooms
        
