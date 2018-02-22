"""
Given two sparse matrices(most elements are 0s) A and B, return the result of AB.

You may assume that A's column number is equal to B's row number.

Example:

A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]


     |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                  | 0 0 1 |
"""
"""
Algorithm:
1. matrix A = m*n (row = i, col = j), matrix B = n*l (j * k)
2. Iterate matrix A (for i, for j), if matrix[i][j] != 0,  iterate matrix B (for k),
if matrix[j][k] != 0 C = A * B
T: O(m*n*l), S: O(m*l)
"""
"""
@param {int[][]} A
@param {int[][]} B
@return {int[][]}
"""
def multiple(A, B):
    if A == None or B == None:
        return [[]]
    m = len(A)
    n = len(A[0])
    l = len(B[0])

    C = [[0 for _ in range(l)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if A[i][j] != 0:
                for k in range(l):
                    if B[j][k] != 0:
                        C[i][k] += A[i][j] * B[j][k]
    return C

if __name__=="__main__":
    A = [
        [1, 0],
        [2, 0],
        [3, 1]
    ]
    B = [
        [0, 1, 0],
        [1, 1, 1],
    ]
    print(multiple(A, B))
"""
    [
        [0, 1, 0],
        [0, 2, 0],
        [1, 4, 1]
    ]
"""
