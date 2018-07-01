"""
Given a string, find the length of the longest substring T that contains at most k distinct characters.

For example, Given s = “eceba” and k = 2,

T is "ece" which its length is 3.
"""
"""
Algorithm: Sliding Window
Use counter to track the number of distinct characters within the slide window

Template reference:
def findSubstring(s):
    // 1. Construct charCount
    charCount = [0] * 128

    // 2. Declare variables
    counter = 0 // count char used
    start = 0 // track window start index
    end = 0 // track window end index
    sub_str_len //  update sub_str_len

    while end < len(s):
        charCount[ord(s[end]) - ord('a')] -= 1 <- BEFORE or AFTER if statement TBD
        if charCount[ord(s[end]) - ord('a')] ?:
            // 3. Modify counter here

        while // 4. Counter condition:
            // 5. Update sub_str_len here if finding minimum

            charCount[ord(s[start]) - ord('a')] += 1 <- BEFORE or AFTER if statement TBD
            if charCount[ord(s[start]) - ord('a')] ?:
                // 6. Modify counter here

            start += 1

        // 7. Update sub_str_len here if finding maximum
        end += 1

    return sub_str_len

T: O(n)
S: O(1)
"""
"""
@param {str} s
@param {int} k
@return {int} max_length
"""
def lengthOfLongestSubstringKDistinct(s, k):
    if len(s) == 0 or k <= 0:
        return 0

    charCount = [0] * 128
    counter = 0
    start = 0
    end = 0
    max_length = 0
    while end < len(s):
        if charCount[ord(s[end]) - ord('a')] == 0:
            counter += 1

        # THIS LINE MUST BE RUN EVERY TIME IN WHILE, MUST CHECK IT SHOULD RUN BEFORE
        # OR AFTER IF STATEMENT
        charCount[ord(s[end]) - ord('a')] += 1

        while counter > k:
            if charCount[ord(s[start]) - ord('a')] == 1:
                counter -= 1

            # THIS LINE MUST BE RUN EVERY TIME IN WHILE, MUST CHECK IT SHOULD RUN
            # BEFORE OR AFTER IF STATEMENT
            charCount[ord(s[start]) - ord('a')] -= 1

            start += 1

        max_length = max(max_length, end - start + 1)
        end += 1

    return max_length
