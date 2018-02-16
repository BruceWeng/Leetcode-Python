"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4.
Note that there may be more than one LIS combination, it is only necessary for you to return the length.

Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?
"""
"""
Algorithm1: DP
1. Initial maxLen int[1] in size of len(nums)
2. Iterate nums
    for i in range(0, len(nums))
        for j in range(0, i)
            Check if nums[i] > nums[j]: maxLen[i] = max(maxLen[j] + 1, maxLen[i])
3. Find the max value in maxLen and return the value

T: O(n^2), S: O(n)
Time Limit Exceeded
"""
def lengthOfLIS(nums):
    if nums == None or len(nums) == 0:
        return 0
    maxLen = [1] * len(nums)

    for i in range(0, len(nums)):
        for j in range(0, i):
            if nums[i] > nums[j]:
                maxLen[i] = max(maxLen[j] + 1, maxLen[i])
    result = 0
    for length in maxLen:
        if length > result:
            result = length
    return result

"""
Algorithm2: Binary Search + DP
1. Initial minLast int[MaxInt] in size of len(nums) + 1 that storing the smallest number
    in decreasing subsequence
2. Let minLast[0] = MinInt, so that when finding first number in minLast >= nums[0], guarantee
    minLast[1] = nums[0]
3. Binary search minLast[mid] to find the first number > num
4. Iterate nums, index = binarySearch(), minLast[index] = nums[i]
5. Reverse traverse minLast, the first index that minLast[i] != MaxInt is the max length, return i

T: O(nlogn), S: O(n)
Example: [10, 9, 2, 5, 3, 7, 101, 18]
minLast: [min, max, max, max, max, max, max, max, max]
minLast: [min, 10, max, max, max, max, max, max, max]
minLast: [min, 9, max, max, max, max, max, max, max]
minLast: [min, 2, max, max, max, max, max, max, max]
minLast: [min, 2, 5, max, max, max, max, max, max]
minLast: [min, 2, 3, max, max, max, max, max, max]
minLast: [min, 2, 3, 7, max, max, max, max, max]
minLast: [min, 2, 3, 7, 101, max, max, max, max]
minLast: [min, 2, 3, 7, 18, max, max, max, max]
return index of 18: 4
"""
import sys
def lengthOfLIS2(nums):
    if nums == None or len(nums) == 0:
        return 0
    minLast = [sys.maxsize] * (len(nums) + 1)
    minLast[0] = - sys.maxsize - 1

    # find the first number >= num
    def binarySearch(num):
        start = 0
        end = len(minLast) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if minLast[mid] < num:
                start = mid
            else:
                end = mid
        # end always >= num
        return end

    for num in nums:
        # Binary Search, find the first number in minLast >= num
        index = binarySearch(num)
        minLast[index] = num

    for i in range(len(minLast) - 1, -1, -1):
        if minLast[i] != sys.maxsize:
            return i

if __name__=="__main__":
    print(lengthOfLIS2([10, 9, 2, 5, 3, 7, 101, 18])) # 4
