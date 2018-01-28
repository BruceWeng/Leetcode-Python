"""
Given a non-negative integer n, count all numbers with unique digits, x, where
0 ≤ x < 10^n.

Example:
Given n = 2, return 91. (The answer should be the total numbers in the range of
0 ≤ x < 100, excluding [11,22,33,44,55,66,77,88,99])
"""
"""
Corner case:
1. n <= 0 -> 0
2. type(n) not is int -> 0
"""
"""
Algorithm:
Solution 1:
1. result = 10 ** n, whenever find the non-unique digits, result -= 1
2. Iterate in range(10^n), if number > 10 convert number to string and iterate
the string, if find duplicate char, result -= 1

Solution 2:
1. digit(1): 10 (0 - 9)
2. digit(2): 9 * 9 (1 - 9 for ones, 1 - 9 for tens)
3. digit(3): digit(2) * 8
4. digit(4): digit(3) * 7
...
10. digit(10): digit(9) * 1
11. digit(11) == digit(12)... = 0, no unique number when digit over 10
"""
"""
Solution 1:
@param {int} n
@return {int}
Hash table
Time Limit Exceeded
"""
def countNumbersWithUniqueDigits(n):
    if n < 0 or not(type(n) is int):
        return 0

    result = 10 ** n
    for i in range(10 ** n):
        digit = str(i)
        hash_table = {}
        for char in digit:
            if hash_table.get(char):
                result -= 1
                break
            else:
                hash_table[char] = True

    return result

"""
Solution 2:
@param {int} n
@return {int}
DP
"""
def countNumbersWithUniqueDigits2(n):
    if n == 0: return 1

    result = 10
    uniqueDigit = 9
    availabeDigit = 9
    while (n > 1 and availabeDigit > 0):
        uniqueDigit *= availabeDigit
        result += uniqueDigit
        n -= 1
        availabeDigit -= 1
    return result
    
if __name__=="__main__":
    print(countNumbersWithUniqueDigits2(2)) # 91
