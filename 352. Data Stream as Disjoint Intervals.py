"""
Given a data stream input of non-negative integers a1, a2, ..., an, ..., summarize
the numbers seen so far as a list of disjoint intervals.

For example, suppose the integers from the data stream are 1, 3, 7, 2, 6, ...,
then the summary will be:

[1, 1]
[1, 1], [3, 3]
[1, 1], [3, 3], [7, 7]
[1, 3], [7, 7]
[1, 3], [6, 7]
Follow up:
What if there are lots of merges and the number of disjoint intervals are small
compared to the data stream's size?
"""
"""
Algorithm: Min Heap

1. Declare a heap intervals that pop out min key
2. Append interval to heap when addNum called
3. Merge intervals and return newIntevals when getIntervals called
4. return new list by appending all merged intevals in newIntevals

addNum:
  T: heapify: O(logn)
  S: O(1)
getIntervals:
  T: pop: O(1) + O(logn)
     merge: O(n)
  S: newIntervals: O(n)
"""
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

import heapq
class SummaryRanges:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.heap = []


    def addNum(self, val):
        """
        :type val: int
        :rtype: void
        """
        # heap in python does not allow to add same key, check if the key existes before add it
        if val not in (tuples[0] for tuples in self.heap): # <- return a list of tuples[0]
            heapq.heappush( self.heap, (val, Interval(val, val)) )

    def getIntervals(self):
        """
        :rtype: List[Interval]
        """
        mergedIntervals = []

        while len(self.heap) != 0:
            key, currInterval = heapq.heappop(self.heap)

            if len(mergedIntervals) == 0:
                mergedIntervals.append( (key, currInterval) )
            else:
                _, prevInterval = mergedIntervals[-1]
                if prevInterval.end + 1 >= currInterval.start:
                    prevInterval.end = max(prevInterval.end, currInterval.end)
                else:
                    mergedIntervals.append( (key, currInterval) )

        # Update intervals with (key, mergedIntervals)
        self.heap = mergedIntervals

        # Update intervals with (mergedIntervals)
        return list(map(lambda x: x[1], mergedIntervals))
