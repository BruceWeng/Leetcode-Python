"""
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:

Given input matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
Example 2:

Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
],

rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
"""
"""
Algorithm 1:

clockwise rotate
first reverse up to down, then swap the symmetry
1 2 3     7 8 9     7 4 1
4 5 6  => 4 5 6  => 8 5 2
7 8 9     1 2 3     9 6 3

anticlockwise rotate
first reverse left to right, then swap the symmetry
1 2 3     3 2 1     3 6 9
4 5 6  => 6 5 4  => 2 5 8
7 8 9     9 8 7     1 4 7

T: O(n)

Algorithm 2: Directly move numbers
1 2 3     "7" 2 '1'      7 "4" 1
4 5 6  =>  4  5  6  =>  '8' 5 '2'
7 8 9     '9' 2 '3'      9 '6' 3

1  2  3  4      "13" 2  3  '1'     13 "9"  3   1      13  9  "5"  1
5  6  7  8  =>   5   6  7   8  =>  5   6   7  '2' => '14'  6  7   2  =>
9  10 11 12      9   10 11  12    '15' 10  11  12     15  10  11 '3'
13 14 15 16     '16' 14 15 '4'     16  14 '8'  4      16 '12' 18  4

13  9   5   1
14 "10"'6'  2
15 '11''7'  3
16  12  18  4

T: O(n)
"""
"""
@param {int[][]} matrix
@return {void}
"""
def rotate1(matrix):
    # matrix.reverse()
    n = len(matrix)
    for i in range(n // 2):
        # n - 1 - i = ~i
        matrix[i], matrix[~i] = matrix[~i], matrix[i]
    # swap symmetry
    for i in range(len(matrix)):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

"""
@param {int[][]} matrix
@return {void}
"""
def rotate2(matrix):
    n = len(matrix)
    # row
    for i in range(n // 2):
        # column
        for j in range(i, n - 1 - i):
            cache = matrix[i][j]
            # n - 1 - i = ~i
            matrix[i][j] = matrix[~j][i]
            matrix[~j][i] = matrix[~i][~j]
            matrix[~i][~j] = matrix[j][~i]
            matrix[j][~i] = cache
