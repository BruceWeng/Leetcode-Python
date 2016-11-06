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


test = Trie()

test.insert('hello')
test.insert('hey')
print(test.search('hey')) #True
print(test.startsWith('he')) #True
print(test.startsWith('heo')) #False
