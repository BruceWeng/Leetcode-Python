"""
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...
Example 1:
Input: "A"
Output: 1

Example 2:
Input: "AB"
Output: 28

Example 3:
Input: "ZY"
Output: 701
"""
"""
Algorithm: 26 carry to decimal(10 carry)
1. convert string to array reversely as chars[]
2. declare result = 0
3. Iterate chars and result += (ord(chars[i]) - ord("a") + 1) * (26 ** i)
4. return result
"""
"""
@param {str} s
@return {int}
"""
def titleToNumber(s):
    if s == None or len(s) == 0:
        return 0

    chars = s[::-1]
    result = 0
    for i in range(len(chars)):
        result += (ord(chars[i]) - ord("A") + 1) * (26 ** i)

    return result
