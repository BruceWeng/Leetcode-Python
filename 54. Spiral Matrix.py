class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0 or len(matrix[0]) == 0 or matrix == None:
            return []

        x = 0
        y = 0
        row = len(matrix)
        col = len(matrix[0])
        result = []
        while row > 0 and col > 0:
            if row == 1:
                for i in range(col):
                    result.append(matrix[x][y])
                    print x, y
                    y += 1
                break
            if col == 1:
                for i in range(row):
                    result.append(matrix[x][y])
                    print x, y
                    x += 1
                break
            for i in range(col-1):
                result.append(matrix[x][y])
                y += 1

            for i in range(row-1):
                result.append(matrix[x][y])
                x += 1

            for i in range(col-1):
                result.append(matrix[x][y])
                y -= 1

            for i in range(row-1):
                result.append(matrix[x][y])
                x -= 1

            row -= 2
            col -= 2
            x += 1
            y += 1

        return result

test1 = [[1, 2], [3, 4]]
test2 = [[1, 2, 3],[4, 5, 6], [7, 8, 9]]
test3 = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]]
test4 = [[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]]
sol = Solution()
print sol.spiralOrder(test4)
