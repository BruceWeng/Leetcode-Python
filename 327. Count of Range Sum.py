"""
Given an integer array nums, return the number of range sums that lie in [lower, upper] inclusive.
Range sum S(i, j) is defined as the sum of the elements in nums between indices i and j (i ≤ j), inclusive.

Note:
A naive algorithm of O(n^2) is trivial. You MUST do better than that.

Example:

Input: nums = [-2,5,-1], lower = -2, upper = 2,
Output: 3
Explanation: The three ranges are : [0,0], [2,2], [0,2] and their respective sums are: -2, -1, 2.
"""
"""
Algorithm: Brute force
0. Declare count = 0, prefixSum = [0] * (n+1)
1. Construct prefixSum[i] = [0, i), S(i, j) = prefixSum[j] - prefixSum[i]
2. for i < len(nums):
    for j <= i:
        if pSum[j] - pSum[i] >= lower and pSum[j] - pSum[i] <= upper:
            count += 1
3. return count

T: O(n^2)
S: O(1)

Algorithm2: Count while Merge Sort
1. Construct pSum[]
2. Declare sort(start, end): return counts in the range of pSum[start:end]
3. Let mid = start + (end - start) // 2, if mid = start: return 0
4. Recursive update count = sort(start, mid) + sort(mid, end)
5. Count left part of pSum aka pSum[start, mid] that meet lower <= sum <= upper, find upper bound j and lower bound i,
   update count += j - 1
6. Maintain the order of pSum array by pSum[lo:hi] = sorted(pSum[lo:hi])
7. Return count

Ex:
nums = [-2,5,-1]
lower = -2
upper = 2

first = [0, -2, 3, 2]

lo = 0
hi = 4 (len(first))
mid = 2
count = sort(0, 2) + sort(2, 4)

In function sort(0, 2):
lo = 0
hi = 2
mid = 1
i = mid = 1
j = mid = 1
left in [0, -2]
first[i] - left = (-2) - 0 = -2 !< -2
first[j] - left = (-2) - 0 = -2 <= 2
j += 1 = 2
first[j] - left = (-2) - (-2) = 0 !< -2
count += 2 - 1 = 1
first[0:2] = sorted(first[0:2])
first = [-2, 0, 3, 2]

In function sort(2, 4):
lo = 2
hi = 4
mid = 3
i = j = mid = 3
first[i] - left = 2 - 3 = -1 !< -2
first[j] - left = 2 - 3 = -1 <= 2
j += 1 = 4
first[j] - left = 2 - 2 = 0 !< -2
count += 4 - 3 = 2
first[2:4] = sorted(first[2:4])
first = [-2, 0, 2, 3]

"""
"""
@param {int[]} nums
@param {int} lower
@param {int} upper
@return {int} count
"""
def countRangeSum(nums, lower, upper):
    first = [0]
    for num in nums:
        first.append(first[-1] + num)
    def sort(lo, hi):
        mid = (lo + hi) // 2
        if mid == lo: # Only one value in the array
            return 0
        count = sort(lo, mid) + sort(mid, hi)
        i = mid
        j = mid
        for left in first[lo:mid]:
            # Compare elements in left half to elements in right half, i is how
            # many numbers that not qualified
            while i < hi and first[i] - left < lower:
                i += 1
            # Compare elements in left half to elements in right half, j is how
            # many numbers that qualified
            while j < hi and first[j] - left <= upper:
                j += 1
            count += j - i
        # Merge step in merge sort, preserve order of the element of two indexs
        # Destructuring
        # sorted: Timsort implementation in Python
        """
        I think this method will only count the case when i is less than j.
        Because for merge sort, we first split the array into two halves, sort
        then separately, and then merge them together, so after sorting, even
        though the indexes are messed up in each half array, but any element
        in the right half will have index larger than any element in the left.
        And in this method, each time after sort, we only compare element in
        the right half with element in the left half, so the i < j requirement
        will be naturally satisfied...
        """
        first[lo:hi] = sorted(first[lo:hi])
        return count
    return sort(0, len(first))

nums = [-2,5,-1]
lower = -2
upper = 2
print(countRangeSum(nums, lower, upper)) # 3
