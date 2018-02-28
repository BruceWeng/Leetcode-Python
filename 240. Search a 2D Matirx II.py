"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
For example,

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.
"""
"""
Algorithm:
1. Search start from left bottom element:
    i = row - 1, j = 0, matrix[i][j]
2. while i >= 0 and j <= col - 1:
    if matrix[i][j] < target: j += 1
    elif matrix[i][j] > target: i -= 1
    else: return True
3. return False if target not found
"""
"""
@param {int[][]} matrix
@param {int} target
@return {bool}
"""
def searchMatrix(matrix, target):
    if target == None or len(matrix) == 0 or len(matrix[0]) == 0:
        return False

    row = len(matrix)
    col = len(matrix[0])
    i = row - 1
    j = 0
    while i >= 0 and j <= col - 1:
        if matrix[i][j] < target:
            j += 1
        elif matrix[i][j] > target:
            i -= 1
        else:
            return True
    return False
