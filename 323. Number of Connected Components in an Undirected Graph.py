class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        if n == 0:
            return 0

        # Init Graph
        graph = [set() for i in range(n)]
        # Build Graph
        for k, v in edges:
            graph[k].add(v)
            graph[v].add(k)

        visited = set()
        count = 0
        print graph
        # Step1: Traverse graph from 0 to n-1, if i not in visited: update visited.add(i), else: dfs
        # Step2: Everytime exit dfs count += 1
        def dfs(i):
            if i in visited:
                return

            visited.add(i)
            for j in graph[i]:
                dfs(j)

        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1

        return count

test1 = [[0, 1], [1, 2], [2, 3], [3, 4]]
sol = Solution()
print sol.countComponents(5, test1) #1
test2 = [[0, 1], [1, 2], [3, 4]]
print sol.countComponents(5, test2) #2
