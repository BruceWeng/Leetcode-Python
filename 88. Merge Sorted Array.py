"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold
additional elements from nums2. The number of elements initialized in nums1 and nums2 are m
and n respectively.
"""
"""
@param {int[]} nums1
@param {int} m: number of elements in nums1
@param {int[]} nums2
@param {int} n: number of elements in nums2
@return {void} modify nums in-place
"""
def merge(nums1, m, nums2, n):
    ptr1 = m - 1
    ptr2 = n - 1
    while ptr1 >= 0 and ptr2 >= 0:
        if nums1[ptr1] >= nums2[ptr2]:
            nums1[ptr1 + ptr2 + 1] = nums1[ptr1]
            ptr1 -= 1
        else:
            nums1[ptr1 + ptr2 + 1] = nums2[ptr2]
            ptr2 -= 1
    # all the numbers in nums1 are moved to the end
    while ptr2 >= 0:
        nums1[ptr2] = nums2[ptr2]
        ptr2 -= 1
    # if all the numbers in nums1 are moved to the end, numbers in nums1 are in right place
