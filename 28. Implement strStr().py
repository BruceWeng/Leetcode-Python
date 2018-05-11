"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle
is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question
to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string.
This is consistent to C's strstr() and Java's indexOf().
"""
"""
Algorithm:
1. Iterate in range(len(haystack) - len(needle) + 1)
(from index 0 to m - n + 1)
2. if haystack[i:i+len(needle)] == needle: return i
3. else return -1
4. if len(needle) == 0 return 0
T: O(mn)
S: O(1)
"""
"""
@param {string} haystack
@param {string} needle
@return {int}
"""
def strStr(haystack, needle):
    if len(needle) == 0:
        return 0

    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i+len(needle)] == needle:
            return i

    return -1
