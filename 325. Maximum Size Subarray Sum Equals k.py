"""
Given an array nums and a target value k, find the maximum length of a subarray
that sums to k. If there isn't one, return 0 instead.

Note:
The sum of the entire nums array is guaranteed to fit within the 32-bit signed integer range.

Example 1:

Input: nums = [1, -1, 5, -2, 3], k = 3
Output: 4
Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.
Example 2:

Input: nums = [-2, -1, 2, 1], k = 1
Output: 2
Explanation: The subarray [-1, 2] sums to 1 and is the longest.
Follow Up:
Can you do it in O(n) time?
"""
"""
Algorithm: Prefix Sum
0. Declare sum_val = 0, max_len = 0
1. Declare prefix_sum to store prefix_sum[i]
2. Declare a hashmap(prefix_sum[i], index) by update hashmap(prefix_sum, index)
3. For each index, check not only curr sum but also currSum - preSum to see if any equals k,
   and update max_len
4. return max_len
"""
"""
@param {int[]} nums
@param {int} k
@param {int} max_len
"""
def maxSubArrayLen(nums, k):
    if len(nums) == 0:
        return 0

    hashmap = {}
    prefix_sum = 0
    max_len = 0
    # Update nums to prefix sum
    for i in range(len(nums)):
        prefix_sum +=  nums[i]

        if prefix_sum == k:
            max_len = i + 1
        elif (prefix_sum - k) in hashmap:
            max_len = max(max_len, i - hashmap[prefix_sum - k])

        if prefix_sum not in hashmap:
            hashmap[prefix_sum] = i

    return max_len
