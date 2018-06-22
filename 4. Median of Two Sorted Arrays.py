"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should
be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""
"""
Algorithm: Binary Search
0. Median is dividing a set into two equal length subsets, that one subset is
   always greater than the other.
1. Partition two arrays into num1_left, num1_right, num2_left and num2_right and
   make sure:
   m + n is even: len(num1_left) + len(num2_left) == len(num1_right) + len(num2_right)
   m + n is odd: len(num1_left) + len(num2_left) == len(num1_right) + len(num2_right) + 1
   len(num1_left) and len(num1_right) do not need to be the same and
   len(num2_left) and len(num2_right) do not need to be the same
2. To guarentee all the elements in the left is less or equal to all the elements in the right,
   a. num1_left[-1] <= num2_right[0]
   b. num2_left[-1] <= num1_right[0]
3. even: median = avg(max(num1_left[-1], num2_left[-1]), min(num1_right[0], num2_right[0]))
   odd: median = max(num1_left[-1], num2_left[-1])
4. Do binary search to find the partition point for num1 and num2 where every
   left elements are less and equal to right elements and meet step 2.

T: O(log(min(m, n)))

Use two pointers to indicate the the range (stare, end) and two pointers
(num1_left_len, num2_left_len) to indicate the partition point, no extra space
S: O(1)
"""
import sys
def findMedianSortedArrays(nums1, nums2):
    # Make sure nums1.length always less than nums2.length
    if len(nums1) > len(nums2):
        return findMedianSortedArrays(nums2, nums1) # <- REMEMBER TO RETURN

    m = len(nums1)
    n = len(nums2)

    if m == 0:
        return nums2[n//2] if n % 2 == 1 else (nums2[n/2-1] + nums2[n/2]) / 2.0

    if n == 0:
        return nums1[m//2] if m % 2 == 1 else (nums1[m/2-1] + nums1[m/2]) / 2.0

    start = 0
    end = m

    while start <= end:
        # nums1_left_len + nums2_left_len = (m + n + 1) // 2
        nums1_left_len = (start + end) // 2 # <- KEY HERE
        nums2_left_len = (m + n + 1) // 2 - nums1_left_len

        # If nums1_left_len == 0, no elements in left side, use -INF as nums1_left_max
        # If nums1_right_len == 0 aka nums1_left_len == m, no elemets in right side, use INF as nums1_right_min
        nums1_left_max = -sys.maxsize if nums1_left_len == 0 else nums1[nums1_left_len-1]
        nums1_right_min = sys.maxsize if nums1_left_len == m else nums1[nums1_left_len]

        # Same logic for nums2
        nums2_left_max = -sys.maxsize if nums2_left_len == 0 else nums2[nums2_left_len-1]
        nums2_right_min = sys.maxsize if nums2_left_len == n else nums2[nums2_left_len]

        # If we find final partition point for both arrays, return median
        if nums1_left_max <= nums2_right_min and nums2_left_max <= nums1_right_min:
            if (m + n) % 2 == 0:
                return (max(nums1_left_max, nums2_left_max) + min(nums1_right_min, nums2_right_min)) / 2.0

            else:
                return max(nums1_left_max, nums2_left_max)

        # If the partition point is too far on right side for nums1, go on left side
        elif nums1_left_max > nums2_right_min:
            end = nums1_left_len - 1

        # If the partition point is too far on left side for nums1, go on right side
        else: # nums2_left_max > nums1_right_min
            start = nums1_left_len + 1

input1 = [1, 2, 3, 5, 6]
input2 = [4]
print(findMedianSortedArrays(input1, input2)) # 3.5
