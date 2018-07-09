"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

Example:

Input: "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
"""
"""
Algorithm: DP
1. Declare isPalindrome: [[bool]] to store s[start:end] is palindrome or not
(start is row, end is col)
2. Declare cuts[int] to store valid palindrome cuts

3. "abcba"
    s   e
    if s[start] == s[end] and end - start <= 2 or isPal[start+1][end-1]:
        isPal[start][end] = True
        Update cuts[]
4. return cuts[length]

T: O(n^2)
S: O(n^2)
"""
"""
@param {str} s
@return {int}
"""
def minCut(s):
    if len(s) == 0:
        return 0

    length = len(s)
    isPal = [[False for _ in range(length)]for _ in range(length)]
    cuts = [0 for _ in range(length)]

    for end in range(length):
        minVal = end
        for start in range(end+1):
            if s[start] == s[end] and (end - start < 2 or isPal[start+1][end-1]):
                isPal[start][end] = True
                if start == 0:
                    minVal = 0
                else:
                    minVal = min(minVal, cuts[start-1] + 1)

        cuts[end] = minVal

    return cuts[length-1]
