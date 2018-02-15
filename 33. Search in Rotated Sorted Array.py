"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to
you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index,
otherwise return -1.

You may assume no duplicate exists in the array.
"""
"""
Algorithm: Binary Search
    /
   /
[ /
       / ]
      /
     /
0. Don't think about cut in LHS or RHS, consider the most naiive condition to trim
1. if nums[mid] == target: return mid
2. if nums[start] < nums[mid]:
       if nums[start] < target < nums[mid]:
           end = mid
       else:
           start = mid
3. if nums[start] > nums[mid]:
       if nums[mid] < target < nums[end]:
           start = mid
       else:
           end = mid
4. after binary search:
    a. if nums[start] == target: return start
    b. elif nums[end] == target: return end
    c. else: return -1

T: O(logn), S: O(1)
"""
"""
@param {int[]} nums
@param {int} target
@return {int} index
"""
def search(nums, target):
    if nums == None or len(nums) == 0 or target == None:
        return -1
    start = 0
    end = len(nums) - 1
    while start + 1 < end:
        mid = start + (end - start) // 2
        if nums[mid] == target:
            return mid
        if nums[start] < nums[mid]:
            # Remember to add equal sign
            if nums[start] <= target < nums[mid]:
                end = mid
            else:
                start = mid
        if nums[start] > nums[mid]:
            # Remember to add equal sign
            if nums[mid] < target <= nums[end]:
                start = mid
            else:
                end = mid

    if nums[start] == target:
        return start
    if nums[end] == target:
        return end
    return -1

if __name__=="__main__":
    print(search([4, 5, 6, 7, 0, 1, 2], 5)) # 1
