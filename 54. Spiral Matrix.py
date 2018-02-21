"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].
"""
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0 or len(matrix[0]) == 0 or matrix == None:
            return []

        rowStart = 0
        rowEnd = len(matrix) - 1
        colStart = 0
        colEnd = len(matrix[0]) - 1
        result = []

        while rowStart <= rowEnd and colStart <= colEnd:
            for i in range(colStart, colEnd + 1):
                result.append(matrix[rowStart][i])
            rowStart += 1

            for i in range(rowStart, rowEnd + 1):
                result.append(matrix[i][colEnd])
            colEnd -= 1

            # Skip if all the elements are put in the result
            if rowStart > rowEnd or colStart > colEnd:
                break

            for i in range(colEnd, colStart - 1, -1):
                result.append(matrix[rowEnd][i])
            rowEnd -= 1

            for i in range(rowEnd, rowStart - 1, -1):
                result.append(matrix[i][colStart])
            colStart += 1

        return result

test1 = [['A', 'B'], ['C', 'D']]
test2 = [[1, 2, 3],[4, 5, 6], [7, 8, 9]]
test3 = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]]
test4 = [[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]]
sol = Solution()
print(sol.spiralOrder(test2))
