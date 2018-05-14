"""
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1
Note:

Your algorithm should run in O(n) time and uses constant extra space.
"""
"""
Algorithm:
Solution 1:
a. Sort the array
b. Iterate the array, if array[i] > 0 and array[i] != array[i-1], return array[i-1] + 1

T: O(nlogn)
S: O(1)

Solution 2:
Move each positive element between range (0 - nums.length) to its inorder position. Ex: 5 should be at index 4
a. Iterate array, if element > 0 and element < n and array[array[i]-1](the correct position) != array[i]
    swap(array[i], array[array[i]-1])
b. To find the first positive, decalare global i = 0, iterate array, if array[i] != i+1: return i+1
c. Else, all the elements are not missing, return i + 1

T: O(n)
S: O(1)
"""
"""
@param {int[]} nums
@return {int}
"""
def firstMissingPositive(nums):
    if nums == None or len(nums) == 0:
        return 1

    def swap(nums, start, end):
        temp = nums[start]
        nums[start] = nums[end]
        nums[end] = temp

    for i, val in enumerate(nums):
        while nums[i] > 0 and nums[i] < len(nums) and nums[nums[i] - 1] != nums[i]:
            swap(nums, nums[i] - 1, i)

    i = 0
    for i, val in enumerate(nums):
        if nums[i] != i + 1:
            return i + 1

    return i + 1

if __name__ == "__main__":
    test1 = [1,2,0]
    test2 = [3,4,-1,1]
    test3 = [7,8,9,11,12]
    test4 = [-1,4,2,1,9,10]
    print(firstMissingPositive(test1)) # 3
    print(firstMissingPositive(test2)) # 2
    print(firstMissingPositive(test3)) # 1
    print(firstMissingPositive(test4)) # 3
