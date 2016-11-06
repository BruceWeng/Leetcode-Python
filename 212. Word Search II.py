class Solution(object):
    def findWords(self, board, words):
        result = []
        row = len(board)
        col = len(board[0])
        if row == 0 or board == None or words == []:
            return result

        trie = Trie()
        for word in words:
            trie.insert(word)

        visited = [[False for y in range(col)] for x in range(row)]

        def traverse(x, y, findWord):
            if x < 0 or x >= row or y < 0 or y >= col:
                return
            if visited[x][y]: return

            newWord = findWord + board[x][y]
            if not trie.startsWith(newWord):
                return

            if trie.search(newWord):
                result.append(newWord)

            visited[x][y] = True
            traverse(x - 1, y, newWord)
            traverse(x + 1, y, newWord)
            traverse(x, y - 1, newWord)
            traverse(x, y + 1, newWord)
            visited[x][y] = False

        for i in range(row):
            for j in range(col):
                traverse(i, j, '')

        return list(set(result))



class TrieNode():
    def __init__(self):
        self.children = {}
        self.isWord = False

class Trie():
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for letter in word:
            child = curr.children.get(letter)
            if child == None:
                child = TrieNode()
                curr.children[letter] = child
            curr = child

        curr.isWord = True

    def search(self, word):
        curr = self.root
        for letter in word:
            child = curr.children.get(letter)
            if child == None:
                return False
            curr = child

        return curr.isWord

    def startsWith(self, prefix):
        curr = self.root
        for letter in prefix:
            child = curr.children.get(letter)
            if child == None:
                return False
            curr = child

        return True


words1 = ['oath', 'pea', 'eat', 'rain']
board2 = [
    ['o', 'a', 'a', 'n'],
    ['e', 't', 'a', 'e'],
    ['i', 'h', 'k', 'r'],
    ['i', 'f', 'l', 'v']
]

board2 = ["baabab","abaaaa","abaaab","ababba","aabbab","aabbba","aabaab"]
words2 = ["bbaabaabaaaaabaababaaaaababb","aabbaaabaaabaabaaaaaabbaaaba","babaababbbbbbbaabaababaabaaa","bbbaaabaabbaaababababbbbbaaa","babbabbbbaabbabaaaaaabbbaaab","bbbababbbbbbbababbabbbbbabaa","babababbababaabbbbabbbbabbba","abbbbbbaabaaabaaababaabbabba","aabaabababbbbbbababbbababbaa","aabbbbabbaababaaaabababbaaba","ababaababaaabbabbaabbaabbaba","abaabbbaaaaababbbaaaaabbbaab","aabbabaabaabbabababaaabbbaab","baaabaaaabbabaaabaabababaaaa","aaabbabaaaababbabbaabbaabbaa","aaabaaaaabaabbabaabbbbaabaaa","abbaabbaaaabbaababababbaabbb","baabaababbbbaaaabaaabbababbb","aabaababbaababbaaabaabababab","abbaaabbaabaabaabbbbaabbbbbb","aaababaabbaaabbbaaabbabbabab","bbababbbabbbbabbbbabbbbbabaa","abbbaabbbaaababbbababbababba","bbbbbbbabbbababbabaabababaab","aaaababaabbbbabaaaaabaaaaabb","bbaaabbbbabbaaabbaabbabbaaba","aabaabbbbaabaabbabaabababaaa","abbababbbaababaabbababababbb","aabbbabbaaaababbbbabbababbbb","babbbaabababbbbbbbbbaabbabaa"]
solution = Solution()
print(solution.findWords(board2, words2))
