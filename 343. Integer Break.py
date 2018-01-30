"""
Given a positive integer n, break it into the sum of at least two positive integers
and maximize the product of those integers. Return the maximum product you can get.

For example, given n = 2, return 1 (2 = 1 + 1); given n = 10, return 36 (10 = 3 + 3 + 4).

Note: You may assume that n is not less than 2 and not larger than 58.
"""
"""
Algorithm:
n = 2 -> 1
n = 3 -> 2
n = 4 -> 4
When i > 4, i * (i-3) > (i//2) ^ 2

T: O(n), S: O(n) -> O(1)
"""
"""
@param {int} n
@return {int}
"""
def integerBreak(n):
    if n < 2: return 0
    if n == 2: return 1
    if n == 3: return 2
    if n == 4: return 4

    result = [2, 3, 4] # [None, None, 2, 3, 4]
    for i in range(5, n+1):
        result[i % 3 - 2] = result[i % 3 - 2] * 3 # result[i] = result[i - 3] * 3
    return result[n % 3 - 2] # result[n]

if __name__=="__main__":
    print(integerBreak(10)) # 36
