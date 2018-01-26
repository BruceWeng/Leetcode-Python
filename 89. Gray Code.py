"""
The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code,
print the sequence of gray code. A gray code sequence must begin with 0.

For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:

00 - 0
01 - 1
11 - 3
10 - 2

Note:
For a given n, a gray code sequence is not uniquely defined.

For example, [0,2,3,1] is also a valid gray code sequence according to the above definition.
"""
"""
Algorithm:
1. Initial a result list to store numbers, starting with [0]
2. Iterate from elements in result in reversed order, result.append(result[j] | 1 << i)
   i: digit number, j: result index
EX: n = 3
result: [0, 1, 11, 10, 110, 111, 101, 100, 1100, 1101, 1111, 1110, 1010, 1011, 1001, 1000]
"""
"""
@param {int} n
@return {int[]}
"""
def grayCode(n):
    result = [0]
    for i in range(n):
        size = len(result)
        for j in range(size - 1, -1, -1):
            result.append(result[j] | 1 << i)
    return result

if __name__=="__main__":
    print(grayCode(3))
    print(grayCode(4))
