"""
Given an unsorted array, find the maximum difference between the successive
elements in its sorted form.

Return 0 if the array contains less than 2 elements.

Example 1:

Input: [3,6,9,1]
Output: 3
Explanation: The sorted form of the array is [1,3,6,9], either
             (3,6) or (6,9) has the maximum difference 3.
Example 2:

Input: [10]
Output: 0
Explanation: The array contains less than 2 elements, therefore return 0.
Note:

You may assume all elements in the array are non-negative integers and fit in the
32-bit signed integer range.
Try to solve it in linear time/space.
"""
"""
Algorithm1: Sorting
1. Sort the array
2. Iterate the array and store the maximum difference from two adjacent numbers
3. return max_diff

T: O(nlogn)
S: O(1)

Algorithm2: Bucket Sort
1. Suppose there are N elements in the array, the min value is min and the max
   value is max. Then the maximum gap will be no smaller than
   (max - min) * 1.0 / (N - 1).
   Ex: [1, 5, 10], max_diff must >= (10-1)*1.0/2 = 4.5, edge case: each element
   evenly distributed.
2. Gap = (max - min) * 1.0 / (N - 1), distribute all numbers in N-1 buckets by put
   num in int((num - min) / gap)th bucket
3. There will be minBuckets[N] update min in this bucket and
                 maxBuckets[N] update max in this bucket
4. max_diff happens when minBuckets[i] - maxBuckets[i-1]
   (the only case for adjacent numbers across the bucket)
5. Return max_diff

T: O(n)
S: O(n)
Ex:
Input: [3,6,9,1]
min = 1
max = 9
localMin: [maxsize, maxsize, maxsize, maxsize]
localMax: [-maxsize, -maxsize, -maxsize, -maxsize]
gap = (max-min) * 1.0 / (N-1)) = 8.0 / 3 = 8/3

i = 0:
index = int((num-min)/gap) = int((3-1)/(8/3)) = int(3/4) = 0
localMin[index] = min(num, localMin[index]) = localMin[0] = min(3, maxsize) = 3
localMax[index] = max(num, localMax[index]) = localMax[0] = max(3, -maxsize) = 3

i = 1:
index = int((num-min)/gap) = int((6-1)/(8/3)) = int(15/8) = 1
localMin[index] = min(num, localMin[index]) = localMin[1] = min(6, maxsize) = 6
localMax[index] = max(num, localMax[index]) = localMax[1] = max(6, -maxsize) = 6

i = 2:
index = int((num-min)/gap) = int((9-1)/(8/3)) = 3
localMin[index] = min(num, localMin[index]) = localMin[3] = min(9, maxsize) = 9
localMax[index] = max(num, localMax[index]) = localMax[3] = max(9, -maxsize) = 9

i = 3:
index = int((num-min)/gap) = int((1-1)/(8/3)) = 0
localMin[index] = min(num, localMin[index]) = localMin[0] = min(1, 3) = 1
localMax[index] = max(num, localMax[index]) = localMax[0] = max(1, 3) = 3

localMin = [1, 6, maxsize, 9]
localMax = [3, 6, -maxsize, 9]

max_diff = localMin[1] - localMax[0] = 6 - 3 or
           localMin[3] - localMax[1] = 9 - 6
if meet maxsize in localMin[] or -maxsize in localMax[]: continue
"""
"""
@param {int[]} nums
@return {int}
"""
import sys
def maximumGap(nums):
    if nums == None or len(nums) <= 1:
        return 0

    max_diff = 0
    maxsize = sys.maxsize
    minsize = -sys.maxsize
    n = len(nums)
    localMin = [maxsize] * n
    localMax = [minsize] * n

    maxVal = minsize
    for num in nums:
        maxVal = max(maxVal, num)

    minVal = maxsize
    for num in nums:
        minVal = min(minVal, num)

    gap = (maxVal - minVal) * 1.0 / (n-1)

    if gap == 0:
        return 0

    for num in nums:
        idx = int((num - minVal) / gap)
        localMin[idx] = min(num, localMin[idx])
        localMax[idx] = max(num, localMax[idx])

    preIdx = 0
    for i in range(n):
        global preIdx
        if localMin[i] == maxsize and localMax[i] == minsize:
            continue

        max_diff = max(max_diff, localMin[i] - localMax[preIdx])
        preIdx = i

    # Update last index for localMax[i]
    max_diff = max(max_diff, maxVal - localMax[preIdx])
    return max_diff
