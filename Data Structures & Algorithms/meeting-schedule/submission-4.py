"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        inters = set()
        for interval in intervals:
            s, e = interval.start, interval.end
            if (s, e) in inters:
                return False
            for start, end in inters:
                if start == s and end < e:
                    return False
                if start < s < end:
                    return False
                if start < e < end:
                    return False
            inters.add((s, e))
        return True
