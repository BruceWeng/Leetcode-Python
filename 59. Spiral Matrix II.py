"""
Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

For example,
Given n = 3,

You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""
"""
@param {int} n
@return {int[][]}
"""
def generateMatrix(n):
    if n == 0 or n == None:
        return []

    # Initial 2D array
    matrix = [[0 for _ in range(n)] for _ in range(n)]

    rowStart = 0
    rowEnd = n - 1
    colStart = 0
    colEnd = n - 1
    num = 1 # Starting number

    while rowStart <= rowEnd and colStart <= colEnd:
        for i in range(colStart, colEnd + 1):
            matrix[rowStart][i] = num
            num += 1
        rowStart += 1

        for i in range(rowStart, rowEnd + 1):
            matrix[i][colEnd] = num
            num += 1
        colEnd -= 1

        for i in range(colEnd, colStart - 1, -1):
            matrix[rowEnd][i] = num
            num += 1
        rowEnd -= 1

        for i in range(rowEnd, rowStart - 1, -1):
            matrix[i][colStart] = num
            num += 1
        colStart += 1
    return matrix

if __name__=="__main__":
    print(generateMatrix(3))
