'''
Consider three strings:text, prefix, and suffix. For each substring, sub, of text, we define the text_score as follows:
- prefix_score = the highest n such that the first n characters of sub are equal to the last n characters of prefix and occur in the same exact order.
- suffix_score = the highest n such that last n characters of sub are equal to the first n characters of suffix and occur in the same eaxct order.
- text_score = prefix_score + suffix_score

For example, if sub = "nothing", prefix = "bruno", and suffix = "ingenious":
- prefix_score = 2 because sub = "nothing" and prefix = "bruno" both have a substring, "no" that is common to the beginning of sub and the end of prefix, and "no" has length n = 2.
- suffix_score = 3 because sub = "nothing" and suffix = "ingenious" both have a substring, "ing", that is common to the end of sub and the beginning of suffix, and "ing" has length n = 3.
- text_score = prefix_score + suffix_score = 2 + 3 = 5

Complete the calculateScore function in the editor below. It has three parameters:
1. A string, text.
2. A string, prefix.
3. A string, suffix.
The function must return a string denoting the non-empty substring of text having a maximal text_score. If there are multiple such substrings, choose the lexicographically smallest substring.

Input Format
The first line contains a string denoting text.
The second line contains a string denoting prefix.
The third line contains a string denoting suffix.

Sample Input 0:
nothing
bruno
ingenious

Sample Output 0:
nothing

Sample Input 1:
ab
b
a

Sample Output 1:
a

Explanation 1:
Given text = "ab", our possible substrings are sub = "a", sub = "b", and sub = "ab"

- sub = "a"
    - predix = "b": The beginning of sub doesn't match the end of prefix, so prefix_score = 0.
    - suffix = "a": The last character of sub mathes the first character of suffix = "a": The last character of sub matchers the first character of suffix, so suffix_score = 1.
    - text_score = prefix_score + suffix_score = 0 + 1 = 1
- sub = "b"
    - prefix = "b": The first character of sub mathces the last characters of prefix, so prefix_score = 1.
    - suffix = "a": The end of sub doesn't match the begining of suffix, sosuffix_score = 0.
    - text_score = prefix_score + suffix_score = 1 + 0 = 1
-sub = "ab"
    - prefix = "b": The beginning of stub doesn't match the end of prefix, so prefix_score = 0.
    - suffix = "a": The last character of sub matches the first character of suffix, so suffix_score = 1
    _ text_score = prefix_score + suffix_score = 0 + 1 = 1
'''
