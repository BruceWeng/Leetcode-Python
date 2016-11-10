'''
1. inDegree Map:
    key: node, value: inDegree (node.label doesn't matter, store node reference id)
2. for curr in inDegree Map
    if value == 0:
        dfs()
3. dfs():
    reault.append(curr)
    inDegree[curr] -= 1 -> -1

    for child in curr.neighbor:
        inDegree[child] -= 1
        if value == 0:
            dfs()
'''

# Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    """
    @param graph: A list of Directed graph node
    @return: A list of graph nodes in topological order.
    """
    def topSort(self, graph):
        # write your code here
        result = []
        inDegree = {}

        for curr in graph:
            inDegree[curr] = 0

        for curr in graph:
            for child in curr.neighbors:
                inDegree[child] += 1

        for curr in graph:
            if inDegree[curr] == 0:
                self.dfs(curr, result, inDegree)

        return result

    def dfs(self, node, result, inDegree):
        result.append(node)
        inDegree[node] -= 1
        for child in node.neighbors:
            inDegree[child] -= 1
            if inDegree[child] == 0:
                self.dfs(child, result, inDegree)

graph0 = DirectedGraphNode(0)
graph1 = DirectedGraphNode(1)
graph2 = DirectedGraphNode(2)
graph3 = DirectedGraphNode(3)
graph4 = DirectedGraphNode(4)
graph5 = DirectedGraphNode(5)

graph0.neighbors.append(graph1)
graph0.neighbors.append(graph2)
graph0.neighbors.append(graph3)
graph1.neighbors.append(graph4)
graph2.neighbors.append(graph4)
graph2.neighbors.append(graph5)
graph3.neighbors.append(graph4)
graph3.neighbors.append(graph5)

graph = []
graph.append(graph0)
graph.append(graph1)
graph.append(graph2)
graph.append(graph3)
graph.append(graph4)
graph.append(graph5)

solution = Solution()
print solution.topSort(graph)
