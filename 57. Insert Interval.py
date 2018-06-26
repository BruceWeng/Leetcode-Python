"""
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
"""
"""
Algorithm:
0. Declare global variable index to tracking the intervals in following traversal
1. Given non-overlapping intervals,
   interval in intervals:
       once interval.end < newInterval.start: gurantee the interval in non-overlapping
       no matter the outcome of newInterval after merging (Because newInterval.start
       either come from newInterval.start or otherInterval.start and both are > interval.end)
   a: result.append(interval)
   b: index += 1
2. Merge overlapping intervals:
   interval in intervals:
    once interval.start <= newInterval.end, gurantee the interval in overlapping(all the interval here
    meet the criterion interval.end >= newInterval.start)
    a. newInterval = new Interval(minimum start, maximum end) (start and end are from interval and newInterval)
    b. index += 1
3. Add the newInterval into result:
    result.append(newInterval)
4. Add all the rest intervals in the result

Note: This algorithm works and not element missing under the condition all the intervals are sorted
by interval.start by default

T: O(n)
S: O(n)
"""

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
"""
@param {Interval[]} intervals
@param {Interval} newInterval
@param {Interval[]}
"""
def insert(intervals, newInterval):
    result = []
    index = 0
    # 1.
    while index < len(intervals) and intervals[index].end < newInterval.start:
        result.append(intervals[index])
        index += 1

    # 2.
    while index < len(intervals) and intervals[index].start <= newInterval.end:
        newInterval = Interval(min(newInterval.start, intervals[index].start), max(newInterval.end, intervals[index].end))
        index += 1
    
    result.append(newInterval)

    # 3.
    while index < len(intervals):
        result.append(intervals[index])
        index += 1
    return result
