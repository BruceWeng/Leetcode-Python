"""
Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

Example 1:

nums = [
  [9,9,4],
  [6,6,8],
  [2,1,1]
]
Return 4
The longest increasing path is [1, 2, 6, 9].

Example 2:

nums = [
  [3,4,5],
  [3,2,6],
  [2,2,1]
]
Return 4
The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
"""
"""
Algorithm:
1. Do DFS from every cell
2. Compare every 4 direction and skip cells that are out of boundary or smaller
3. Get matrix max from every cell's max
4. Use cache[m][n] to memorize max distance
5. In DFS function, when move to 4 direction, if matrix[new position][new position] <= matrix[i][j],
skip the route, so we don't need a visited[m][n]
6. THE KEY IS to cache the distance because it's highly possible to revisit a cell
"""
"""
@param {int[][]} matrix
@return {int} distance
"""
def longestIncreasingPath(matrix):
    if matrix == None or len(matrix) == 0 or len(matrix[0]) == 0:
        return 0

    m = len(matrix)
    n = len(matrix[0])
    cache = [[0 for _ in range(n)] for _ in range(m)]
    distance = 1
    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    def dfs(i, j):
        if cache[i][j]:
            return cache[i][j]
        distance = 1
        for direction in directions:
            x = i + direction[0]
            y = j + direction[1]
            if x < 0 or x >= m or y < 0 or y >= n or matrix[x][y] <= matrix[i][j]:
                continue
            length = 1 + dfs(x, y)
            distance = max(distance, length)
        cache[i][j] = distance
        return distance

    for i in range(m):
        for j in range(n):
            length = dfs(i, j)
            distance = max(distance, length)

    return distance

if __name__=="__main__":
    test1 = [[9, 9, 4], [6, 6, 8], [2, 1, 1]]
    test2 = [[3, 4, 5], [3, 2, 6], [2, 2, 1]]
    print(longestIncreasingPath(test1))
    print(longestIncreasingPath(test2))
