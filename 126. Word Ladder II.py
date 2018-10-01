"""
Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return an empty list if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: []

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
"""
import collections
import string
class Solution(object):
    def backtrack(self, neighbor_dict, beginWord, word, result, path):
        if beginWord == word:
            result.append(path)
        else:
            for prev_node in neighbor_dict[word]:
                self.backtrack(neighbor_dict, beginWord, prev_node, result, [prev_node] + path)
            
            
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        
        unvisited = set(wordList)
        if endWord not in unvisited:
            return []
        # do nothing if beginWord is not in set
        unvisited.discard(beginWord)
        
        neighbor_dict = collections.defaultdict(list)
        queue = collections.deque([beginWord])
        # BFS: a variation of Dijkstra's algorithm
        while len(queue):
            print("New queue: " + queue[0])
            visited = set()
            # traverse the whole level of the same ladder length
            for i in range(len(queue)):
                cur = queue.popleft()
                for i in range(len(cur)):
                    for char in string.ascii_lowercase:
                        neighbor = cur[:i] + char + cur[i+1:]
                        if neighbor == cur:
                            continue
                        print(neighbor)
                        if neighbor in unvisited:
                            if neighbor not in visited:
                                visited.add(neighbor)
                                print(visited)
                                queue.append(neighbor)
                            neighbor_dict[neighbor].append(cur)
                            print(neighbor_dict)
            unvisited -= visited
            visited.clear()
            print(visited)
        
        # DFS
        result = []
        self.backtrack(neighbor_dict, beginWord, endWord, result, [endWord])
        return result

beginWord = "hit";
endWord = "cog";
wordList = ["hot","dot","dog","lot","log","cog"]
solution = Solution()
print(solution.findLadders(beginWord, endWord, wordList))
        