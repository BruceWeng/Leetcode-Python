"""
Write an efficient algorithm that searches for a value in an m x n matrix.
This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true.
"""
"""
Algorithm: Binary search, treat as a sorted array
1. let start and end be index
2. find target with matrix[mid // cols][mid % cols]
T: O(m*nlogm*n), S: O(1)
"""
"""
@param {int[][]} matrix
@param {int} target
@return {bool}
"""
def searchMatrix(matrix, target):
    if target == None or len(matrix) == 0 or len(matrix[0]) == 0:
        return False

    start = 0
    rows = len(matrix)
    cols = len(matrix[0])
    end = rows * cols - 1
    while start + 1 < end:
        mid = start + (end - start) // 2
        value = matrix[mid // cols][mid % cols]
        if value == target:
            return True
        if value < target:
            start = mid
        else:
            end = mid
    if matrix[start // cols][start % cols] == target or matrix[end // cols][end % cols] == target:
        return True
    else:
        return False
