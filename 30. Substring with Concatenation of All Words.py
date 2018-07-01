"""
You are given a string, s, and a list of words, words, that are all of the same length.
Find all starting indices of substring(s) in s that is a concatenation of each word
in words exactly once and without any intervening characters.

Example 1:

Input:
  s = "barfoothefoobarman",
  words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoor" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.
Example 2:

Input:
  s = "wordgoodstudentgoodword",
  words = ["word","student"]
Output: []
"""
"""
Algorithm: sliding window
https://leetcode.com/problems/substring-with-concatenation-of-all-words/discuss/13656/An-O(N)-solution-with-detailed-explanation
T: O(n)
S: O(1)

Too hard to remember, to review the solution again!
"""
"""
@param {str} s
@param {str} words
"""
def findSubstring(s, words):
    if len(s) == 0 or len(words) == 0:
        return []

    need = {}
    for word in words:
        if word not in need:
            need[word] = 0
        else:
            need[word] += 1

    n = len(s)
    num = len(words)
    length = len(words[0])
    result = []

    for i in range(length):
        left = i
        count = 0
        seen = {}
        for j in range(i, n-length+1, length):
            word = s[j:j+length]
            if word in need:
                # Construct seen(word, count)
                if word not in seen:
                    seen[word] = 0
                else:
                    seen[word] += 1

                if seen[word] <= need[word]:
                    count += 1
                else:
                    while seen[word] > need[word]:
                        first = s[left:left+length]
                        left += length
                        # Decrease window seen(first, count)
                        if first not in seen:
                            seen[first] = 0
                        else:
                            seen[first] -= 1

                        # Construct need(first, 0)
                        if first not in need:
                            need[first] = 0

                        if seen[first] < need[first]:
                            count -= 1

                if count == num:
                    result.append(left)
                    count -= 1
                    first = s[left:left+length]
                    left += length
                    seen[first] = seen[first] - 1
            else:
                seen = {}
                count = 0
                left = j + length

    return result
