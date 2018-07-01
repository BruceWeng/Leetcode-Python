"""
Find the length of the longest substring T of a given string (consists of lowercase
letters only) such that every character in T appears no less than k times.

Example 1:

Input:
s = "aaabb", k = 3

Output:
3

The longest substring is "aaa", as 'a' is repeated 3 times.
Example 2:

Input:
s = "ababbc", k = 2

Output:
5

The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
"""
"""
Algorithm Sliding Window

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

1. Need extra variables:
    unique_char_count = 0 (unique char numbers in substring)
    no_less_than_k_char_count = 0 (count how many chars that appear no less than k time in substring)
2. To ensure every chars in substring appear no less than k times:
    unique_char_count == no_less_than_k_char_count

3. Need to enumerate from all the characters with unique_char_count_target (1-26)
3.a Wrap the sliding window in for loop

T: O(n) (O(26n))
S: O(1)
"""
"""
@param {str} s
@param {int} k
@return {int} max_length
"""
def lengthOfLongestSubstring(s, k):
    if len(s) == 0:
        return 0

    result = 0
    for unique_char_count_target in range(1, 26):

        charCount = [0] * 128

        unique_char_count = 0
        no_less_than_k_char_count = 0
        start = 0
        end = 0
        max_length = 0

        while end < len(s):
            indexEnd = ord(s[end]) - ord('a')
            if charCount[indexEnd] == 0:
                unique_char_count += 1

            charCount[indexEnd] += 1

            if charCount[indexEnd] == k:
                no_less_than_k_char_count += 1
            end += 1

            while unique_char_count > unique_char_count_target:
                indexStart = ord(s[start]) - ord('a')
                if charCount[indexStart] == k:
                    no_less_than_k_char_count -= 1

                charCount[indexStart] -= 1

                if charCount[indexStart] == 0:
                    unique_char_count -= 1
                start += 1

            if unique_char_count == unique_char_count_target and unique_char_count == no_less_than_k_char_count:
                max_length = max(max_length, end - start)


        result = max(result, max_length)

    return result
