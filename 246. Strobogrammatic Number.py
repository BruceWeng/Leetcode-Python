"""
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to determine if a number is strobogrammatic. The number is represented as a string.

Example 1:

Input:  "69"
Output: true
Example 2:

Input:  "88"
Output: true
Example 3:

Input:  "962"
Output: false
"""
"""
Algorithm: HashMap, Two pointers
1. Declare a hashmap(str(number), str(strobogrammatic number))
    ("0", "0"), ("1", "1"), ("6", "9"), ("8", "8"), ("9", "6")
2. Declare left = 0 and right = num.length - 1
3. while left <= right:
    if num[left] not in hashMap: return false
    if hashMap[num[left]] != num[right]: return false

    left += 1
    right -= 1

4. return true
"""
"""
@param {string} num
@return {bool}
"""
def isStrobogrammatic(num):
    if num == None or len(num) == 0:
        return False

    hashMap = {}
    hashMap["0"] = "0"
    hashMap["1"] = "1"
    hashMap["6"] = "9"
    hashMap["8"] = "8"
    hashMap["9"] = "6"

    left = 0
    right = len(num) - 1

    while left <= right:
        if num[left] not in hashMap:
            return False

        if hashMap[num[left]] != num[right]:
            return False

        left += 1
        right -= 1

    return True
