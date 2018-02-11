"""
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?
"""
"""
Algorithm:
Solution 1. kth row only depends on (k-1)th row, we only need to maintain
k + k + 1 = 2k + 1 elements, S: O(k)
Solution 2. Update kth row starting from j == i, maintain only k elements, S(k)
"""
"""
@param {int} rowIndex
@return {int[]}
"""
def getRow(rowIndex):
    if rowIndex < 0:
        return []

    result = [0] * (rowIndex + 1)
    result[0] = 1

    for i in range(1, rowIndex + 1):
        for j in range(i, 0, -1):
            result[j] += result[j - 1]
    return result

if __name__=="__main__":
    print(getRow(3))
