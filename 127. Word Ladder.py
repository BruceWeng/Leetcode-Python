"""
Given two words (beginWord and endWord), and a dictionary's word list, find the
length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a
transformed word.
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log", "cog"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Note:
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
UPDATE (2017/1/20):
The wordList parameter had been changed to a list of strings (instead of a set
of strings). Please reload the code definition to get the latest changes.
"""
"""
Algorithm: Graph, BFS
a. Consider every word as a node
b. When s1 can transformed into s2 by changin one character, make connection between s1 and s2
c. Given s1 and s2, now problem transfered into find shortest path between s1 and s2
d. Use BFS for traversal

1. Find all neighbor nodes from current node
    i. Traverse each char x in current word and change the char x to a different one in a-z to
    form a new word2, check if word2 in wordList. Time: O(26*w), w = len(word)
2. Label node that has been visited: remove word from wordList
3. Once find the endWord in BFS, how to find path from backtracking? With tuple(word, length)

Note:
1. If endWord not in wordList return 0
2. Remove beginWord in wordList to prevent revisit
"""
"""
@param {string} beginWord
@param {string} endWord
@param {string[]} wordList
@return {int}
"""
import collections
def ladderLength(beginWord, endWord, wordList):
    if beginWord == None or len(beginWord) == 0 or endWord == None or len(endWord) == 0 \
    or wordList == None or len(wordList) == 0 or endWord not in wordList:
        return 0

    wordSet = set(wordList)
    if beginWord in wordSet:
        wordSet.remove(beginWord)
    neighborsQueue = collections.deque([(beginWord, 1)]) # [(node, length)]

    while neighborsQueue:
        word, length = neighborsQueue.popleft()
        if word == endWord:
            return length
        for i in range(len(word)):
            for x in "abcdefghijklmnopqrstuvwxyz":
                if word[i] != x:
                    newWord = word[:i] + x + word[i+1:]
                    if newWord in wordSet:
                        neighborsQueue.append((newWord, length + 1))
                        wordSet.remove(newWord)
    return 0

if __name__=="__main__":
    beginWord = "a"
    endWord = "c"
    wordList = ["a", "b", "c"]
    print(ladderLength(beginWord, endWord, wordList))
