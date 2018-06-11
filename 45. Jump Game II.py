"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example:

Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.
Note:

You can assume that you can always reach the last index.
"""
"""
Algorithm: BFS, each node: (index, value)
                  node                      min_jump
                 (0, 2)                     [0, 0, 0, 0, 0]
               /        \
            (1, 3)      (2, 1)              [0, 1, 1, 0, 0]
          /    |    \        \
    (2, 1)  (3, 1)  (4, 4)  (3, 1)          [0, 1, 1, 2, 2]
       |       |    return 2   |
    (3, 1)  (4, 4)          (4, 4)
       |    return 3        return 3
    (4, 4)
    return 4

1. Decalre level = 0, curr_level_last_idx = 0, next_level_last_idx = 0
2. Iterate nums and update next_level_last_idx = Math.max(next_level_last_idx, nums[i] + 1)
    if next_level_last_idx reaches last index, return level + 1
3. If i > curr_level_last_idx: no solution, return -1
"""
"""
@param {int[]} nums
@return {int}
"""
def jump(nums):
    if len(nums) <= 1:
        return 0

    level = 0
    curr_level_last_idx = 0 # Mark last element index in curr level
    i = 0
    while i <= curr_level_last_idx:
        next_level_last_idx = curr_level_last_idx # Mark last element index in next level
        while i <= curr_level_last_idx:
            next_level_last_idx = max(next_level_last_idx, nums[i] + i)

            if next_level_last_idx >= len(nums) - 1:
                return level + 1

            i += 1
        level += 1
        curr_level_last_idx = next_level_last_idx

    # If i > curr_level_last_idx, i can not move forwar anymore
    # (the last element in the array can't be reached)
    return - 1

input1 = [1, 2, 3]
print(jump(input1))
input2 = [1, 2, 1, 1, 1]
print(jump(input2))
