"""
Given two strings s and t, determine if they are both one edit distance apart.

Note:

There are 3 possiblities to satisify one edit distance apart:

Insert a character into s to get t
Delete a character from s to get t
Replace a character of s to get t
Example 1:

Input: s = "ab", t = "acb"
Output: true
Explanation: We can insert 'c' into s to get t.
Example 2:

Input: s = "cab", t = "ad"
Output: false
Explanation: We cannot get t from s by only one step.
Example 3:

Input: s = "1203", t = "1213"
Output: true
Explanation: We can replace '0' with '1' to get t.
"""
"""
Algorithm:
1. if abs(s.length - t.length) > 1: return false
2. Iterate through index in range(min(s.length, t.length))
Case 1: Replace 1 char(when s.length == t.length):
    s: a B c
    t: a D c
Case 2: Delete 1 char in s:
    s: a B c
    t: a   c
Case 3: Insert 1 char in s (a.k.a Delete a char in t):
    s: a   c
    t: a B c

3. Handle edge case: one more letter after iteration
(All previous chars are the same, the only possibility is deleting the end char
in the longer one of s and t)
"""
"""
@param {str} s
@param {str} t
@return {bool}
"""
def isOneEditDistance(s, t):
    if s == None or t == None or abs(len(s) - len(t)) > 1:
        return False

    for i in range(min(len(s), len(t))):
        if s[i] != t[i]:
            # case 1
            if len(s) == len(t):
                return s[i+1:] == t[i+1:]
            # case 2
            elif len(s) > len(t):
                return s[i+1:] == t[i:]
            # case 3
            else:
                return s[i:] == t[i+1:]

    # Handle edge case
    return abs(len(s) - len(t)) == 1
