"""
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
"""
"""
@param {Interval[]} intervals
@return {Interval[]}
"""
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

def merge(intervals):
    if intervals == None or len(intervals) == 0:
        return []
    result = []
    # Sort by ascending starting point
    intervals = sorted(intervals, key=lambda i: i.start)

    # Move start and end rather than merge inteval, when
    # non-overlapping occur, append new Interval with start and end
    start = intervals[0].start
    end = intervals[0].end
    for i in intervals:
        if i.start <= end :
            end = max(i.end, end)
        else:
            result.append(Interval(start, end))
            start = i.start
            end = i.end

    # Append last Interval(start, end)
    result.append(Interval(start, end))
    return result
