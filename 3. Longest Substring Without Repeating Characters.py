"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer
must be a substring, "pwke" is a subsequence and not a substring.
"""
"""
Algorithm: Sliding Window
1. Declare hashmap(char, index), update hashmap wilte traversing the string s
2. Declare max_legnth to store max length of substring and update it while traversing
the string s
3. Traverse s starting with end = 0,
    if s[end] in hashmap:
        start = max(start, hashmap[s[end]] + 1)
    else:
        Update hashmap[char] = index
        Update max_legnth = max(max_legnth, end-start+1)
4. return max_legnth

T: O(n)
S: O(1)
"""
"""
@param {str} s
@return {int} max_length
"""
def lengthOfLongestSubstring(s):
    if len(s) == 0:
        return 0

    hashmap = {} #(char, index)
    max_length = 0
    end = 0
    start = 0
    for _ in range(len(s)):
        if s[end] in hashmap:
            start = max(start, hashmap[s[end]] + 1)

        hashmap[s[end]] = end
        max_length = max(max_length, end-start+1)

        end += 1

    return max_length
