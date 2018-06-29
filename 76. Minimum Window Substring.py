"""
Given a string S and a string T, find the minimum window in S which will contain
all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty
string "".
If there is such window, you are guaranteed that there will always be only one
unique minimum window in S.
"""
"""
Algorithm: Hashmap + Two pointers
1. Declare charCount int[128] and construct key value pairs (index: ord(char) - ord('a'), value: counts in T)
2. Declare counter = 0: count how many characters in T we have not used in S
           start = 0: window start index, used to recover charCount[c] and counter -= 1
           end = 0: window end index, used to decrement charCount[c] and counter += 1
           min_len = sys.maxsize: accumulator to update the min_substr_length
           head = 0: final window head, update when find valid window start index
3. Iterate s and decrement charCount[S[end]], if charCount[S[end]] >= 0 after decrement(valid character), counter += 1(use one char in T)
4. while counter == len(T):
    update min_len by end - start + 1 and update head = start
    4.a If S[start] in charCount: charCount[S[start]] += 1
    4.b If charCount[S[start]] > 0: counter -= 1 (More chars allowed to use)
    4.c start += 1
5. If min_len == sys.maxsize: return "" else return S[head:head+min_len]
"""
"""
@param {str} s
@param {str} t
@return {str}
"""
import sys
def minWindow(s, t):
    charCount = [0] * 128
    for c in t:
        charCount[ord(c) - ord('a')] += 1

    counter = 0
    start = 0
    end = 0
    min_len = sys.maxsize
    head = 0
    while end < len(s):
        charCount[ord(s[end]) - ord('a')] -= 1
        if charCount[ord(s[end]) - ord('a')] >= 0:
            counter += 1

        while counter == len(t):
            if end - start + 1 < min_len:
                min_len = end - start + 1
                head = start

            charCount[ord(s[start]) - ord('a')] += 1
            if charCount[ord(s[start]) - ord('a')] > 0:
                counter -= 1

            start += 1

        end += 1

    if min_len == sys.maxsize:
        return ""
    else:
        return s[head:head+min_len]

"""
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
