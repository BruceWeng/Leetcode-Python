class TrieNode():
    def __init__(self):
        self.children = {}
        self.isWord = False
        self.size = 0

class Trie():
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        curr = self.root
        for letter in word:
            child = curr.children.get(letter)
            if child == None:
                child = TrieNode()
                curr.children[letter] = child
            child.size += 1
            curr = child
        curr.isWord = True

    def find(self, prefix):
        curr = self.root
        for letter in prefix:
            child = curr.children.get(letter)
            if child == None:
                return 0
            curr = child
        return curr.size

def solveContacts(oper):
    trie = Trie()
    for data in oper:
        if data[0] == 'add':
            trie.add(data[1])
        elif data[0] == 'find':
            print(trie.find(data[1]))

def main():
    n = int(input())
    operations = []
    for i in range(n):
        data = input().split(' ') #array
        operations.append(data) #array of array of size 2 [op, word]

    solveContacts(operations)
if __name__ == '__main__':
    main()
