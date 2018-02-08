"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

For example,
Given [[0, 30],[5, 10],[15, 20]],
return 2.
"""
"""
Algorithm:
Min-Heap Solution:
1. Sort the intervals by start time
2. Use a min heap to track the min end time of merged intervals
3. Start with the first meeting, put it to a meeting room(heap)
4. Iterate intervals starting from i = 1
5. If the current meeting(intervals[i]) start time > heap[0].end time, there's no need for a new room, merge the interval
6. Otherwise, this meeting needs a new room, put intervals[i] in meeting room(heap)
7. return len(heap) (number of meeting rooms)
"""
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
"""
@param {Interval[]} intervals
@return {int}
"""
import heapq
def minMeetingRooms(intervals):
    if intervals == None or len(intervals) == 0:
        return 0

    intervals.sort(key=lambda interval: interval.start)
    heap = []
    # Since heapq has no key param, push only end time in heap
    heap.append(intervals[0].end)
    for i in range(1, len(intervals)):
        if intervals[i].start >= heap[0]:
            # heap[0] to peek is read only, directly modify heap[0] can not maintain the order
            heapq.heappop(heap)
            heapq.heappush(heap, intervals[i].end)
        else:
            heapq.heappush(heap, intervals[i].end)

    return len(heap)

if __name__=="__main__":
    interval1 = Interval(0, 30)
    interval2 = Interval(5, 10)
    interval3 = Interval(15, 20)
    print(minMeetingRooms([interval1, interval2, interval3])) # 2
