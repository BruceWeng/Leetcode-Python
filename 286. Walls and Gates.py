from collections import deque
import sys
class Solution(object):
    #Solution1: T: O(mn)
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        #1. Traverse the grid, if find a '0', start to BFS the nearby INF
        #2. Store coordinates and distance from '0' in tuple and append to queue when reach new grid elements
        if not rooms or len(rooms) == 0 or len(rooms[0]) == 0:
            return

        queue = deque()
        m = len(rooms)
        n = len(rooms[0])
        inf = sys.maxint

        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue.append((i, j))

        while queue:
            x, y = queue.popleft()
            if x < m-1 and rooms[x + 1][y] == inf:
                rooms[x + 1][y] = rooms[x][y] + 1
                queue.append((x + 1, y))

            if x > 0 and rooms[x - 1][y] == inf:
                rooms[x - 1][y] = rooms[x][y] + 1
                queue.append((x - 1, y))

            if y < n-1 and rooms[x][y + 1] == inf:
                rooms[x][y + 1] = rooms[x][y] + 1
                queue.append((x, y + 1))

            if y > 0 and rooms[x][y - 1] == inf:
                rooms[x][y - 1] = rooms[x][y] + 1
                queue.append((x, y - 1))

        return rooms

    #Solution2: Traverse and Prune, T(mn)
    def wallsAndGates2(self, rooms):
        if not rooms or len(rooms) == 0 or len(rooms[0]) == 0:
            return

        m = len(rooms)
        n = len(rooms[0])

        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue = deque()
                    queue.append((i + 1, j, 1))
                    queue.append((i - 1, j, 1))
                    queue.append((i, j + 1, 1))
                    queue.append((i, j - 1, 1))
                    while queue:
                        x, y, val = queue.popleft()
                        if x < 0 or x >= m or y < 0 or y >= n or rooms[x][y] < val:
                            continue

                        rooms[x][y] = val
                        queue.append((x + 1, y, val + 1))
                        queue.append((x - 1, y, val + 1))
                        queue.append((x, y + 1, val + 1))
                        queue.append((x, y - 1, val + 1))

        return rooms

inf = sys.maxint
test1 = [[inf, -1, 0, inf],[inf, inf, inf, -1],[inf, -1, inf, -1],[0, -1, inf, inf]]
test2 = [[0, inf, inf, inf, 0]]
sol = Solution()
print sol.wallsAndGates2(test1)
