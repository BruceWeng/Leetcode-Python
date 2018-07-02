"""
Given an array of meeting time intervals consisting of start and end times
[[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

Example 1:

Input: [[0,30],[5,10],[15,20]]
Output: false
Example 2:

Input: [[7,10],[2,4]]
Output: true
"""
"""
Algorithm: Sorting
1. Sort array by interval start times
2. If array[i].start < array[i-1].end: return false
3. Return true

T: O(nlogn)
S: O(1)
"""
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
def canAttendMeetings(intervals):
    # list.sort() sort intervals in-place
    intervals.sort(key=lambda x: x.start)

    for i in range(1, len(intervals)):
        # allow duplicate time, use less rather than less and equal
        if intervals[i].start < intervals[i-1].end:
            return False

    return True
