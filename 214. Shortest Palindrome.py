"""
Given a string s, you are allowed to convert it to a palindrome by adding characters
in front of it. Find and return the shortest palindrome you can find by performing
this transformation.

Example 1:

Input: "aacecaaa"
Output: "aaacecaaa"
Example 2:

Input: "abcd"
Output: "dcbabcd"
"""
"""
Algorithm1: Three pointers
1. Declare i: to indicate valid palindrome head, j: to indicate valid palindrome tail
2. Declare start: to indicate the final index suffix s[start:] to be reversed and add to the front of s
3. while i < j:
    If s[i] == s[j]:
        i += 1
        j -= 1
    else:
        i = 0
        start -= 1
        j = start
4. return reverse(s[start + 1:]) + s

Ex1: aacecaaa

i = 0
j = 7
start = 7
"a a c e c a a a"
s[0] == s[0]

i = 1
j = 6
start = 7
"a a c e c a a a"
s[1] == s[6]

i = 2
j = 5
start = 7
"a a c e c a a a"

a[2] == c
a[5] == a

a[2] != a[5]
i = 0
start = 6
j = 6

i = 0
j = 6
start = 6
"a a c e c a a a"
a[0] == a[6]...

Since we only allow to add string from front. The added must be a reverse of substring
from somewhere index to the end of s. The whole algorithm tries to find
the starting index (start+1) of substring.

T: O(n^2)
S: O(n)

Result: Time Limit Exceeded in Python

Algorithm2: KMP, to be studied if needed

Algorithm3: use s.startswith(substr): return boolean if s startswith substr

Example: s = dedcba. Then r = abcded and I try these overlays (the part in (...)
is the prefix I cut off, I just include it in the display for better understanding):

  s          dedcba
  r[0:]      abcded    Nope...
  r[1:]   (a)bcded     Nope...
  r[2:]  (ab)cded      Nope...
  r[3:] (abc)ded       Yes! Return abc + dedcba

 Note: startswith is written in C, so it compares very fast. There is no magic algorithm
 under the wood.
"""
"""
Algorithm1:
@param {str} s
@return {str}
"""
def shortestPalindrome(s):
    if len(s) == 0:
        return ""

    i = 0
    j = len(s) - 1
    start = len(s) - 1

    while i < j:
        if s[i] == s[j]:
            i += 1
            j -= 1
        else:
            i = 0
            start -= 1
            j = start

    return s[start+1:][::-1] + s
"""
Algorithm3:
@param {str} s
@return {str}
"""
def shortestPalindrome(s):
    r = s[::-1]
    for i in range(len(s) + 1):
        if s.startswith(r[i:]):
            return r[:i] + s
