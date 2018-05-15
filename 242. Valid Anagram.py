"""
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""
"""
Solution 1: HashMap
1. Declare a int[26] as hashmap with index: ord(nums[i]) - ord("a"), value: counts
2. Iterate s and increment hashmap, iterate t and decreasement hashmap
3. Iterate hashmap, if hashmap[i] != 0: return false
4. Return true

T: O(n)
S: O(26)
if inputs contain unicode: S: O(256)

Solution 2: Sorting
1. If sorted(s) == sorted(t): return true, else return false

T: O(nlogn)
S: O(1)
"""
"""
@param {string} s
@param {string} t
@return {bool}
"""
def isAnagram(s, t):
    if s == None or t == None or len(s) != len(t):
        return False

    hashmap = [0] * 26
    for i in range(len(s)):
        hashmap[ord(s[i]) - ord("a")] += 1
        hashmap[ord(t[i]) - ord("a")] -= 1

    for count in hashmap:
        if count != 0:
            return False

    return True
