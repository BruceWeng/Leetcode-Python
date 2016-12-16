# Solution 1:
# 1. The root locates in the longest path from leaves
# 2. BFS from leaves, remove any node that indegree is 1, the remaining 1 or 2 nodes are roots
# 3. Use set() in adjList for constant time remove

# Solution 2:
# DP: current height = min(neighbor heights) + 1

class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 0:
            return []
        # list of sets
        adjList = [set() for i in range(n)]
        for k, v in edges:
            adjList[k].add(v)
            adjList[v].add(k)
        # list of numbers
        leaves = [i for i in range(n) if len(adjList[i]) <= 1]
        while n > 2:
            n -= len(leaves)
            newLeaves = []
            # i: numbers in list
            for i in leaves:
                # j: numbers in set
                for j in adjList[i]:
                    adjList[j].remove(i)
                    if len(adjList[j]) == 1:
                        newLeaves.append(j)
            leaves = newLeaves
        return leaves

test1 = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
sol = Solution()
print sol.findMinHeightTrees(6, test1)
