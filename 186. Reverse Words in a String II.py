"""
Given an input string , reverse the string word by word.

Example:

Input:  ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
Note:

A word is defined as a sequence of non-space characters.
The input string does not contain leading or trailing spaces.
The words are always separated by a single space.
Follow up: Could you do it in-place without allocating extra space?
"""
"""
Algorithm:
Three step reverse
1. Reverse the whole array
2. Reverse each word:
    if s[i] == " ": reverse(s, start, i - 1)
    start += 1
3. Reverse the last word(special case because there is no space after the last word)
This will solve the case if there is only one word

* Wirte a independant reverse(s, start, end) function

T: O(n)
S: O(1)
"""
"""
@param {char[]} s
@return {void}
"""
def reverseWords(s):
    if len(s) == 0:
        return

    def reverse(string, start, end):
        while start < end:
            temp = string[start]
            string[start] = string[end]
            string[end] = temp
            start += 1
            end -= 1

    start = 0
    # 1. reverse the whole array
    reverse(s, 0, len(s) - 1)

    # 2. reverse each word
    for i, val in enumerate(s):
        if s[i] == " ":
            reverse(s, start, i - 1)
            start = i + 1

    # 3. reverse the last word
    reverse(s, start, len(s) - 1)
