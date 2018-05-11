"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:

Input: "Hello World"
Output: 5
"""
"""
Algorithm:
1. Split string by " " into a word array
2. if lastword == " ", return 0
3. Return len(lastword) in the word array
T: O(n)
S: O(n)
"""
"""
@param {string} s
@return {int}
"""
def lengthOfLastWord(s):
    # strip right end of string first
    return len(s.rstrip().split(" ")[-1])
