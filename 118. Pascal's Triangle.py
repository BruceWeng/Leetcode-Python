"""
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""
"""
Algorithm:
1. result = []
2. for i in range(1, numRows + 1) row = []
3.     for j in range(i)
            if j == 0 or j == i - 1, row.append(1),
            otherwise, row[j] = result[i - 1][j - 1] + result[i - 1][j]
4. return result
"""
"""
@param {int} numRows
@return {int[][]}
"""
def generate(numRows):
    if numRows <= 0:
        return []
    result = []

    for i in range(1, numRows + 1):
        row = []
        for j in range(i):
            if j == 0 or j == i - 1:
                row.append(1)
            else:
                # find the i - 2 row (i starts with 1)
                row.append(result[i - 2][j - 1] + result[i - 2][j])
        result.append(list(row))

    return result

if __name__=="__main__":
    print(generate(5))
