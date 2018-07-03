"""
Given an array nums, there is a sliding window of size k which is moving from the
very left of the array to the very right. You can only see the k numbers in the window.
Each time the sliding window moves right by one position. Return the max sliding window.

Example:

Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7]
Explanation:

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Note:
You may assume k is always valid, 1 ≤ k ≤ input array's size for non-empty array.

Follow up:
Could you solve it in linear time?
"""
"""
Algorithm: Two windows
For Example: A = [2,1,3,4,6,3,8,9,10,12,56], w=4

1. partition the array in blocks of size w=4. The last block may have less then w.
    2, 1, 3, 4 | 6, 3, 8, 9 | 10, 12, 56|

2. Traverse the list from start to end and calculate max_so_far. Reset max after each block boundary (of w elements).
    left_max[] = 2, 2, 3, 4 | 6, 6, 8, 9 | 10, 12, 56

3. Similarly calculate max in future by traversing from end to start.
    right_max[] = 4, 4, 4, 4 | 9, 9, 9, 9 | 56, 56, 56

4. now, sliding max at each position i in current window, sliding-max(i) = max{right_max(i), left_max(i+w-1)}
    sliding_max = 4, 6, 6, 8, 9, 10, 12, 56

T: O(n)
S: O(n)
"""
"""
@param {int[]} nums
@param {int} k
@return {int[]}
"""
def slidingWindowMax(nums, k):
    if len(nums) == 0:
        return []

    max_left = [0] * len(nums)
    max_right = [0] * len(nums)

    # Initiate max_eft and max_right
    max_left[0] = nums[0]
    max_right[-1] = nums[-1]

    # Update max_left from head
    for i in range(1, len(nums)):
        max_left[i] = nums[i] if i % k == 0 else max(nums[i], max_left[i-1])

        # Update max_right from tail
        j = len(nums) -i - 1
        max_right[j] = nums[j] if i % k == k-1 else max(nums[j], max_right[j+1])

    sliding_max = [0] * (len(nums) - k + 1)
    i = 0
    j = 0

    while i + k <= len(nums):
        sliding_max[j] = max(max_right[i], max_left[i+k-1])
        i += 1
        j += 1

    return sliding_max
