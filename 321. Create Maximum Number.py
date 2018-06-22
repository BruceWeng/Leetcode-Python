"""
Given two arrays of length m and n with digits 0-9 representing two numbers.
Create the maximum number of length k <= m + n from digits of the two.
The relative order of the digits from the same array must be preserved.
Return an array of the k digits.

Note: You should try to optimize your time and space complexity.

Example 1:

Input:
nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]
k = 5
Output:
[9, 8, 6, 5, 3]
Example 2:

Input:
nums1 = [6, 7]
nums2 = [6, 0, 4]
k = 5
Output:
[6, 7, 6, 0, 4]
Example 3:

Input:
nums1 = [3, 9]
nums2 = [8, 9]
k = 3
Output:
[9, 8, 9]
"""
"""
Algorithm: Greedy + DP
0. To solve the problem, need to solve two subproblems first.
1. maxArray(nums, k): return max k elements(preserve order) in an array
   [Greedy]
    a. Declare number_to_pop = nums.length - k
    b. Declare result = [] which the descending order sequence from the max element
    c. if nums[i] > result[j], number_to_pop -= len(result) - i, result.pop() * number_to_pop,
       result.append(nums[i])
    d. while number_to_pop != 0: do (c)

    T: O(n), Greedy
    S: O(n)
2. merge(nums1, nums2): return an array contains max numbers(preserve order)
   [Greedy]
   from all elements in nums1 and nums2
   WARNING: The following two pointers not work because when meet the case nums1[i] == nums2[j],
   need to compare the next not identical number and put the larger on to result[]
   a. Use two pointers(i, j) to point first elements from nums1 and nums2
   b. Declare result array
   c. result.append(max(nums1[i]), nums2[j]), increment the pointer with bigger value
   d. If i == len(nums1): add all remaining nums2 elements in result, vice versa
   e. return result

   Work solution:
   a. Compare entire array nums1 and nums2, result.append(nums1[0]) if nums1 > nums2, vice versa
   b. Slicing nums1 = nums1[1:] or slicing nums2 = nums2[1:]
   c. return result

   T: O((n+m)^2), Greedy
   S: O(n)
3. Pick up kth elements from result by comparing result[0]*k and result of merge(maxArray(nums1, i), maxArray(nums2, k-i))
   [DP]

   T: O(k)
   S: O(k)

T: O(k*(n+m)^2), worst case, k = n+m, O((n+m)^3)
S: O(n+m)
"""
"""
@param {int[]} nums1
@param {int[]} nums2
@param {int[]}
"""
def maxNumber(nums1, nums2, k):
    n = len(nums1)
    m = len(nums2)

    """
    Return max k elements(preserve order) in an array
    @param {int[]} nums
    @param {int} k
    @return {int[]}
    """
    def maxArray(nums, k):
        result = [0] * k
        j = 0
        for i in range(len(nums)):
            while j > 0 and nums[i] > result[j-1] and len(nums) - i > k - j:
                j -= 1
            if j < k:
                result[j] = nums[i]
                j += 1

        return result
        
    """
    Return an array contains max numbers(preserve order)
    @param {int[]} nums1
    @param {int[]} nums2
    @return {int[]}
    """
    def merge(nums1, nums2):
        result = []

        while nums1 or nums2:
            if nums1 > nums2:
                result.append(nums1[0])
                nums1 = nums1[1:]
            else:
                result.append(nums2[0])
                nums2 = nums2[1:]

        return result

    result = [0] * k
    for i in range(k+1):
        j = k - i

        if i > n or j > m:
            continue

        candidate = merge(maxArray(nums1, i), maxArray(nums2, j))
        # Since both result and candidate guaranteed k long, max returns the
        # greater iterable collection
        result = max(result, candidate)
    return result

nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]
k = 5

print(maxNumber(nums1, nums2, k)) # [9, 8, 6, 5, 3]
