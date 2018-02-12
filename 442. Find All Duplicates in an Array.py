"""
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear
twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
"""
"""
Solution 1: HashMap
S: O(n), not qualified

Solution 2: Sorting
T: O(nlogn), not qualified

Solution 3:
We can use the element constraint, 1 ≤ a[i] ≤ n, which is not element is greater than
the size of the array. That implys elment - 1 can map to index in the array 0 ≤ i ≤ n - 1
1. consider input array as a hashmap that key: abs(num) - 1, value: -array[key]
2. While traversing, if any nums[abs(array[i]-1)] is negative, result.append[array[i]]
3. return result
"""
"""
@param {int[]} nums
@return {int[]}
"""
def findDuplicates(nums):
    if nums == None or len(nums) == 0:
        return []
    result = []
    for num in nums:
        index = abs(num) - 1
        if nums[index] < 0:
            result.append(index + 1)
        else:
            nums[index] *= -1
    return result

if __name__=="__main__":
    print(findDuplicates([4,3,2,7,8,2,3,1])) # [2, 3]
