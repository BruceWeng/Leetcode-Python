"""
Given a string S and a string T, count the number of distinct subsequences of S which equals T.

A subsequence of a string is a new string which is formed from the original string
by deleting some (can be none) of the characters without disturbing the relative
positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Example 1:

Input: S = "rabbbit", T = "rabbit"
Output: 3
Explanation:

As shown below, there are 3 ways you can generate "rabbit" from S.
(The caret symbol ^ means the chosen letters)

rabbbit
^^^^ ^^
rabbbit
^^ ^^^^
rabbbit
^^^ ^^^
Example 2:

Input: S = "babgbag", T = "bag"
Output: 5
Explanation:

As shown below, there are 5 ways you can generate "bag" from S.
(The caret symbol ^ means the chosen letters)

babgbag
^^ ^
babgbag
^^    ^
babgbag
^    ^^
babgbag
  ^  ^^
babgbag
    ^^^
"""
"""
Algorithm: DP
  S 0123....j
T +----------+
  |1111111111|
0 |0         |
1 |0         |
2 |0         |
. |0         |
. |0         |
i |0         |

1. Construct mem[len(T)+1][len(S)+1] with 0
   for col in range(len(S) + 1):
       mem[0][col] = 1
   The first row must be filled with 1. That's because the empty string is a
   subsequence of any string but only 1 time. So mem[0][col] = 1 for every j.
   We can return correct value if T is an empty string.

   The first column of every rows except the first must be 0. This is because an
   empty string cannot contain a non-empty string as a substring -- the very first
   item of the array: mem[0][0] = 1, because an empty string contains the empty string 1 time.


2.1 if T[i-1] == S[j-1]:
        mem[row][col] = mem[row-1][col-1] + mem[row][col-1] (left-up grid + left grid)
    else:
        mem[row][col] = mem[row][col-1] (left grid)

S: [acdabefbc] and T: [ab]
   first we check with a:

           *  *
      S = [acdabefbc]
mem[1] = [0111222222]

then we check with ab:

               *  *
      S = [acdabefbc]
mem[1] = [0111222222]
mem[2] = [0000022244]
And the result is 4, as the distinct subsequences are:

      S = [a   b    ]
      S = [a      b ]
      S = [   ab    ]
      S = [   a   b ]

T: O(n*m), n = len(T), m = len(S)
S: O(n*m)
"""
"""
@param {str} s
@param {str} t
@return {int}
"""
def numDistinct(s, t):
    mem = [[0 for _ in range(len(s) + 1)] for _ in range(len(t) + 1) ]

    for col in range(len(s) + 1):
        mem[0][col] = 1

    for row in range(1, len(t) + 1):
        for col in range(1, len(s) + 1):
            if t[row-1] == s[col-1]:
                mem[row][col] = mem[row-1][col-1] + mem[row][col-1]
            else:
                mem[row][col] = mem[row][col-1]


    return mem[len(t)][len(s)]
