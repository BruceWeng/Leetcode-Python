"""
Given an array of size n, find the majority element. The majority element is the element that appears more than  floor(n/2) times.

You may assume that the array is non-empty and the majority element always exist in the array.
"""
import unittest
"""
@param {array} nums: array of integers
@return {integer} majority element
"""
def majorityElement(nums):
    if nums == None or len(nums) == 0:
        return None
    # Solution 1: T: O(n), S: O(n)
    # Iterate nums and save element frequency in hash table
    frequency = {} # key: element, value: frequency
    for element in nums:
        if element not in frequency:
            frequency[element] = 1
        else:
            frequency[element] += 1
    # Iterate hash table and find the largest value
    max_value = 0
    for key, value in frequency.iteritems():
        if value > max_value: max_value = value
    for key, value in frequency.iteritems():
        if value == max_value: return key

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(majorityElement([1, 1, 2, 3, 3, 3, 3]), 3)
    def test2(self):
        self.assertEqual(majorityElement([1, 1, 1, 1, 1, 2, 2]), 1)

if __name__=="__main__":
    unittest.main()
