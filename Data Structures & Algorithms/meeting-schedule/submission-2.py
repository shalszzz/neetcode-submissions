"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        prev = Interval(0,0)
        new=sorted(intervals, key=lambda x: x.start)
        for meeting in new:
            if meeting.start>=prev.end:
                prev=meeting
            else:
                return False

        return True

