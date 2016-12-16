from collections import deque
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if len(board) == 0:
            return
        m = len(board)
        n = len(board[0])
        queue = deque()

        # Flip 'O' to '*' on the edges
        def flip(x, y, queue):
            if x < 0 or x > m - 1 or y < 0 or y > n - 1 or board[x][y] != 'O':
                return

            queue.append([x, y])
            board[x][y] = '*'

        # BFS on every grid
        def bfs(x, y, queue):
            if board[x][y] == 'O':
                flip(x, y, queue)

            while queue:
                curr = queue.popleft()
                i = curr[0]
                j = curr[1]

                flip(i + 1, j, queue)
                flip(i - 1, j, queue)
                flip(i, j + 1, queue)
                flip(i, j - 1, queue)

        # Traverse first and last row
        for j in range(n):
            bfs(0, j, queue)
            bfs(m - 1, j, queue)

        # Traverse first and last col
        for i in range(1, m - 1):
            bfs(i, 0, queue)
            bfs(i, n - 1, queue)

        # Traverse all grid and flip '*' to 'O', flip 'O' to 'X'
        for i in range(m):
            for j in range(n):
                if board[i][j] == '*':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'

        return board
test1 = [["X","X","X","X"], ["X","O","O","X"], ["X","X","O","X"], ["X","O","X","X"]]
sol = Solution()
print sol.solve(test1)
