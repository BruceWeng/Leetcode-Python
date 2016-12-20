from collections import deque
import sys
class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        #1. Traverse all elements and find numbers of '1's(buildings)
        #2. Init minDist for taking record of minimum distance start from node (i, j)
        #3. Init visited[][] preventing repeating element, oneCount[][] to find the element connect all buildings
        #3. Run BFS start from every elements, if grid[i][j] == 1: find all grid[i][j] == 0 and not visited[i][j]
        #4. BFS function(i, j):
        #5. return min([minDist[i][j] for i in range(m) for j in range(n)]) + 1 where oneCount[i][j] == buildings
        if not grid or len(grid) == 0 or len(grid[0]) == 0:
            return -1

        buildings = 0
        m = len(grid)
        n = len(grid[0])

        minDist = [[0] * n for i in range(m)]
        oneCount = [[0] * n for i in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    buildings += 1
                    queue = deque()
                    queue.append((i, j))
                    visited = [[False] * n for row in range(m)]
                    dist = 0
                    while queue:
                        for k in range(len(queue)):
                            x, y = queue.popleft()
                            minDist[x][y] += dist
                            oneCount[x][y] += 1
                            if x > 0 and grid[x-1][y] == 0 and not visited[x-1][y]:
                                queue.append((x-1, y))
                                visited[x-1][y] = True

                            if x + 1 < m and grid[x+1][y] == 0 and not visited[x+1][y]:
                                queue.append((x+1, y))
                                visited[x+1][y] = True

                            if y > 0 and grid[x][y-1] == 0 and not visited[x][y-1]:
                                queue.append((x, y-1))
                                visited[x][y-1] = True

                            if y + 1 < n and grid[x][y+1] == 0 and not visited[x][y+1]:
                                queue.append((x, y+1))
                                visited[x][y+1] = True
                        dist += 1


        result = sys.maxint
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and oneCount[i][j] == buildings:
                    result = min(result, minDist[i][j])

        if result == sys.maxint:
            return -1
        else:
            return result

test1 = [
    [1, 0, 2, 0 ,1],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0]
]

sol = Solution()
print sol.shortestDistance(test1)
