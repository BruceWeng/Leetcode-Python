"""
Given a string s and a string t, check if s is subsequence of t.

You may assume that there is only lower case English letters in both s and t.
t is potentially a very long (length ~= 500,000) string, and s is a short string (<=100).

A subsequence of a string is a new string which is formed from the original string
by deleting some (can be none) of the characters without disturbing the relative
positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
s = "abc", t = "ahbgdc"

Return true.

Example 2:
s = "axc", t = "ahbgdc"

Return false.

Follow up:
If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want
to check one by one to see if T has its subsequence. In this scenario, how would you change your code?
"""
"""
Algorithm1: Two pointers
1. Declare index_s = 0, index_t = 0
2. while index_s < len(s) and index_t < len(t):
    if t[index_t] === s[index_s]:
        index_s += 1

    index_t += 1
3. return index_s == len(s)

T: O(n), n is the length of t
S: O(1)

Algorithm2: For follow up, there are lots of incomming S:
* Follow-up
  If we check each sk in this way, then it would be O(kn) time
  where k is the number of s and n is the length of t.

  This is inefficient.
  Since there is a lot of s, it would be reasonable to preprocess t to generate
  something that is easy to search for if a character of s is in t.
  Sounds like a HashMap, which is super suitable for search for existing stuff.
"""
"""
@param {str} s
@param {str} t
@return {bool}
"""
def isSubsequence(s, t):
    index_s = 0
    index_t = 0

    while index_s < len(s) and index_t < len(t):
        if s[index_s] == t[index_t]:
            index_s += 1

        index_t += 1

    return index_s == len(s)
