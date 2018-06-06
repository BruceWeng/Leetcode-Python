"""
Given an array of non-negative integers, you are initially positioned at the first
index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.
"""
"""
Algorithm1:
Bottom Up Brute Force:
0. Declare reach(bool[n]) to store if the current index can be reached from
previous indexes

1. Declare two pointers, i = 0 and j = 1, use two loops to validate indicate all
the possible, steps before A[i] that can be reach from j. (reach[i+j] = ture)

2. return reach[n-1]

T: O(n^2)
S: O(n)
Input: [2, 3, 1, 1, 4]

i = 0, j = 1 -> 2:
[2, 3, 1, 1, 4]
 ^
 i
reach: [true, true, true, false, false]
                ^     ^
i = 1, j = 1 -> 3:
[2, 3, 1, 1, 4]
    ^
    i
reach = [true, true, true, true, true]
                       ^     ^     ^

Algorithm2:
Buttom Up Memorization:
Modify Algo1, the reach array must be a continuous true array, store only the farest index
1. Declare k as the farest index
2. k = max(k, i + j), since k stores the max index and max index comes from i + A[i]:
   k = max(k, i + A[i])

 T: O(n)
 S: O(1)
"""
"""
@param {int[]} nums
@return {bool}
"""
"""Algo1"""
def canJump(nums):
    if nums == None or len(nums) == 0:
        return False

    reach = [False] * len(nums)
    reach[0] = True
    for i in range(len(nums)):
        if reach[-1] == True:
            return True
        if reach[i] == False:
            continue
        for j in range(1, nums[i]+1):
            if i + j < len(nums):
                reach[i+j] = True

    return reach[-1]

"""Algo2"""
def canJump(nums):
    if nums == None or len(nums) == 0:
        return False

    k = 0
    for i in range(len(nums)):
        if i <= k:
            k = max(k, i + nums[i])

    return k >= len(nums) - 1
