"""
You have a number of envelopes with widths and heights given as a pair of integers
(w, h). One envelope can fit into another if and only if both the width and height
of one envelope is greater than the width and height of the other envelope.

What is the maximum number of envelopes can you Russian doll? (put one inside other)

Example:
Given envelopes = [[5,4],[6,4],[6,7],[2,3]], the maximum number of envelopes you can
Russian doll is 3 ([2,3] => [5,4] => [6,7]).
"""
"""
Algorithm:
1. Sort the array. Ascend on width and descend on height if width are same.
2. Find the longest increasing subsequence based on height.
Note: Since the width is increasing, we only need to consider height.
[3, 4] cannot contains [3, 3], so we need to put [3, 4] before [3, 3] when sorting
otherwise it will be counted as an increasing number if the order is [3, 3], [3, 4]
"""
"""
@param {int[][]} envelopes
@return {int}
"""
import sys
def maxEnvelopes(envelopes):
    if envelopes == None or len(envelopes) == 0 or envelopes[0] == None or len(envelopes[0]) != 2:
        return 0

    # Sort array ascending on width and descending on height if width are the same.
    envelopes.sort(key=lambda x: (x[0], -x[1]))

    minLast = [sys.maxsize] * (len(envelopes) + 1)
    minLast[0] = -sys.maxsize - 1

    # search the first number >= num
    def binarySearch(target):
        start = 0
        end = len(minLast) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if minLast[mid] < target:
                start = mid
            else:
                end = mid
        # end always >= target
        return end

    for num in envelopes:
        # Binary Search, find the first number in minLast >= num[1]
        index = binarySearch(num[1])
        minLast[index] = num[1]

    for i in range(len(minLast) - 1, -1, -1):
        if minLast[i] != sys.maxsize:
            return i

if __name__=="__main__":
    print(maxEnvelopes([[5,4],[6,4],[6,7],[2,3]])) # 3
