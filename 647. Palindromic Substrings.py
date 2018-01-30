"""
Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different
substrings even they consist of same characters.

Example 1:
Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

Example 2:
Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

Note:
The input string length won't exceed 1000.
"""
"""
Algorithm:
Solution 1: Brute Force
1. Iterate string in nested for loop,
for i in range(len(s)):
    for j in range(len(i)):
        if (validPalindrome(s[i:j])): count += 1
2. Return count
T: O(n^2), S: O(1)

Solution 2: Extend Palindrome
1. Iterate string if for loop and choose s[i] as center of palidrome
2. Call extendPalindrome(left, right) with odd length(i, i) and even length(i, i + 1)
3. Validate palindrome in extendPalidrom while loop, if true, left -= 1, right += 1, count += 1
4. Return count
T: O(n^2), Worst case: "aaaaaa", Best case: "abcde" -> T: O(n), S: O(1)
"""
"""
@param {string} s
@return {int} count
"""
def countSubstrings(s):
    if s == None or len(s) == 0: return 0

    count = [0]
    def extendPalindrome(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
            count[0] += 1

    for i in range(len(s)):
        extendPalindrome(i, i) # Count odd length
        extendPalindrome(i, i + 1) # Count even length

    return count[0]

if __name__=="__main__":
    print(countSubstrings("abc")) # 3
    print(countSubstrings("aaa")) # 6
