"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where
"adjacent" cells are those horizontally or vertically neighboring. The same letter
cell may not be used more than once.

For example,
Given board =

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
"""
"""
Algorithm:
1. Do DFS from every cells, DFS(i, j. word) function return True if found, else return False
2. DFS function:
    1. if len(word) == 0: return True # run out all the characters
    2. return False if cells that are out of boundary or smaller or word[0] != board[i][j]
    3. cache board[i][j]
    4. mark board[i][j] = "*" to prevent revisit
    5. Check the rest of charaters in 4 directions with DFS(i +- 1, j +- 1, word[1:]), if either one is False, return False
    6. Give back cache to board[i][j]
    7. return result(return value of 5.)
"""
"""
@param {int[][]} board
@param {string} word
"""
def exist(board, word):
    if len(board) == 0 or len(board[0]) == 0 or board == None or word == None:
        return False

    def dfs(i, j, word):
        if len(word) == 0:
            return True

        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[0]:
            return False

        cache = board[i][j]
        board[i][j] = "*"
        result = dfs(i + 1, j, word[1:]) or \
                 dfs(i, j + 1, word[1:]) or \
                 dfs(i - 1, j, word[1:]) or \
                 dfs(i, j - 1, word[1:])
        board[i][j] = cache
        return result

    for i in range(len(board)):
        for j in range(len(board[0])):
            if dfs(i, j, word):
                return True
    return False

if __name__=="__main__":
    test = [
      ['A','B','C','E'], \
      ['S','F','C','S'], \
      ['A','D','E','E'] \
    ]
    word1 = "ABCCED"
    word2 = "ABCB"
    print(exist(test, word1)) # True
    print(exist(test, word2)) # False
