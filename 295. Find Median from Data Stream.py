"""
Median is the middle value in an ordered integer list. If the size of the list is even,
there is no middle value. So the median is the mean of the two middle value.

For example,
[2,3,4], the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.
Example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3)
findMedian() -> 2
"""
"""
Algorithm: min heap and max heap
1. Keep teo heaps:
    Max-heap small has the smaller half of the numbers
    Min-heap large has the larger half of the numbers
2. Get median returns:
    Odd: len(large) > len(small):
        return float(larget[0])
    Even:
        return small[0] / 2.0 + large[0] / 2.0

    T: O(1)
3. Add nums:
    T: O(logn) time by heapify
"""
import heapq
class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num):
        heapq.heappush(self.large, num)
        heapq.heappush(self.small, -heapq.heappop(self.large))
        if len(self.large) < len(self.small):
            heapq.heappush(self.large, -heapq.heappop(self.small))

    def findMedian(self):
        # Odd
        if len(self.large) > len(self.small):
            return self.large[0]
        # Even, prevent large number overflow
        else:
            return self.large[0] / 2.0 - self.small[0] / 2.0
