"""
Given a m x n matrix, if an element is 0, set its entire row and column to 0.
Do it in place.
"""
"""
Algorithm:
1. Store states of each row in the first row.
2. Store states of each col in the first col.
EX: if matrix[i][j] = 0: row: matrix[0][j] = 0, col: matrix[i][0] = 0
3. State of row0 and col0 occupy the same cell, use matrix[0][0] to represent state of
row0, and use another variable col0 to represent state of col0
4. Use states to set matrix elements. Use bottom-up direction to prevent mess up
states in matrix[i][0] and matrix[0][j]
T: O(m*n), S: O(1)
"""
"""
@param {int[][]} matrix
@return {void}
"""
def setZeros(matrix):
    if matrix == None or len(matrix) == 0 or len(matrix[0]) == 0:
        return

    col0 = False
    rows = len(matrix)
    cols = len(matrix[0])
    # Store states
    for i in range(rows):
        if matrix[i][0] == 0:
            col0 = True
        for j in range(1, cols):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    for i in range(rows - 1, -1, -1):
        for j in range(cols - 1, 0, -1):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
        if col0: matrix[i][0] = 0
