"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""
"""
Assumption: n and k are positive integers
Corner case:
Input: n <= 0 or k <= 0 -> []
Input: k > n -> []
"""
"""
Algorithm:
1. Initiate result = []
2. Use DFS to traverse from root to children of nodes, numbers of children = k
3. DFS function(current = [], count)
    a. base case:
        if count == k:
            result.append(current)
            return
    b. recursive case:
        for i in range(1, n + 1):
            current.append(i)
            traverse(current, count + 1)
            current.pop()
            ""
* Add pre_number to avoid duplicate numbers in program when coding
"""
"""
@param {int} n
@param {int} k
@return {int[][]}
"""
def combine(n, k):
    if n <= 0 or k <= 0 or k > n:
        return []

    result = []

    def traverse(current, count, pre_number):
        if count == k:
            result.append(list(current))
            return

        for i in range(pre_number + 1, n + 1):
            current.append(i)
            traverse(current, count + 1, i)
            current.pop()

    traverse([], 0, 0)
    return result

if __name__=="__main__":
    print(combine(4, 2))
