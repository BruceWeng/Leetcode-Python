"""
Given a string s , find the length of the longest substring t  that contains at
most 2 distinct characters.

Example 1:

Input: "eceba"
Output: 3
Explanation: t is "ece" which its length is 3.
Example 2:

Input: "ccaabbb"
Output: 5
Explanation: t is "aabbb" which its length is 5.
"""
"""
Algorithm: Sliding Window
Window Substring template:
def findSubstring(s):
    // 1. Construct charCount
    charCount = [0] * 128

    // 2. Declare variables
    counter = 0 // count char used
    start = 0 // track window start index
    end = 0 // track window end index
    sub_str_len //  update sub_str_len

    while end < len(s):
        charCount[ord(s[end]) - ord('a')] -= 1
        if charCount[ord(s[end]) - ord('a')] ?:
            // 3. Modify counter here

        while // 4. Counter condition:
            // 5. Update sub_str_len here if finding minimum

            charCount[ord(s[start]) - ord('a')] += 1
            if charCount[ord(s[start]) - ord('a')] ?:
                // 6. Modify counter here

            start += 1

        // 7. Update sub_str_len here if finding maximum
        end += 1

    return sub_str_len
"""
"""
@param {str} s
@return {int} max_length
"""
def lengthOfLongestSubstringTwoDistinct(s):
    if len(s) == 0:
        return 0

    charCount = [0] * 128
    counter = 0
    start = 0
    end = 0
    max_length = 0
    while end < len(s):
        indexEnd = ord(s[end]) - ord('a')
        if charCount[indexEnd] == 0:
            counter += 1

        charCount[indexEnd] += 1
        end += 1

        while counter > 2:
            indexStart = ord(s[start]) - ord('a')
            if charCount[indexStart] == 1:
                counter -= 1

            charCount[indexStart] -= 1
            start += 1

        max_length = max(max_length, end - start)

    return max_length
