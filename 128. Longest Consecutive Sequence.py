"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
"""
"""
Algorithm: Hash
1. Declare a map(num, max length including the num)
2. Iterate nums:
    if num in map:
        left = map[num - 1]
        right = map[num + 1]
        localMaxLen = left + right + 1(num)
        map[num] = localMaxLen
        map[num-left] = localMaxLen
        map[num+right] = localMaxLen
        maxLen = max(maxLen, localMaxLen)
    else:
        continue
3. Return maxLen
"""
"""
@param {int[]} nums
@return {int}
"""
def longestConsecutive(nums):
    if nums == None or len(nums) == 0:
        return 0

    hashMap = {}
    maxLen = 0
    for num in nums:
        if num not in hashMap:
            if (num - 1) in hashMap:
                left = hashMap[num - 1]
            else:
                left = 0
            if (num + 1) in hashMap:
                right = hashMap[num + 1]
            else:
                right = 0

            localMaxLen = left + right + 1
            hashMap[num] = localMaxLen
            # Extend the length to the boundarys fo the sequence
            # Will do nothing if n has no neighbors
            hashMap[num - left] = localMaxLen
            hashMap[num + right] = localMaxLen
            maxLen = max(maxLen, localMaxLen)
        else:
            continue

    return maxLen
