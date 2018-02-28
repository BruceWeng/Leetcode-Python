"""
Given a n x n matrix where each of the rows and columns are sorted in ascending order,
find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
Note:
You may assume k is always valid, 1 ≤ k ≤ n2.
"""
"""
Algorithm 1: Min Heap
1. Put first row in minheap
2. Pop root of minheap and then add next smallest number into minheap
2.2 Let root coordinates (i, j), next smallest number is (i + 1, j)
2.3 If root (i == len(matrix)-1), add (i+1, j+1)
3. Do 2. for k-1 times
4. return minheap.pop

T: O(klogn), S:O(n)
"""
"""
@param {int[][]} matrix
@param {int} k
@return {int}
"""
import heapq # Min-Heap

def kthSmallest(matrix, k):
    if k <= 0 or len(matrix) == 0 or len(matrix[0]) == 0:
        return 0

    heap = []

    for j, num in enumerate(matrix[0]):
        # heap compare the first element in tuple
        heapq.heappush(heap, (matrix[0][j], 0, j))

    num = 0
    for _ in range(k):
        num, i, j = heapq.heappop(heap)
        if i < len(matrix) - 1:
            heapq.heappush(heap, (matrix[i + 1][j], i + 1, j))

    return num

"""
Algorithm 2: Binary Search
1. Let start = matrix[0][0], end = matrix[-1][-1]
2. Let mid = start + (end - start) // 2, make a function getLessEqual(mid) to find
the index of last number <= mid
3. if index < k: start = mid
4. else index > k: end = mid
5. return end

getLessEqual(val):
Starting from leftbottom number matrix[-1][0]

result = 0
while i >= 0 and j < n
    if matrix[i][j] > val:
        i -= 1
    else:
        result += i + 1
        j += 1
return result

Swap from left-bottom to right-top can get count <= mid in O(n) time instead of
O(nlogn), total complexity will be O(nlogm) while m = end - start.
"""
"""
@param {int[][]} matrix
@param {int} k
@return {int}
"""
def kthSmallest2(matrix, k):
    if k <= 0 or len(matrix) == 0 or len(matrix[0]) == 0:
        return 0

    n = len(matrix)
    start = matrix[0][0]
    end = matrix[-1][-1]

    def getLessEqual(val):
        result = 0
        i = n - 1
        j = 0
        while i >= 0 and j < n:
            if matrix[i][j] > val:
                i -= 1
            else:
                result += i + 1
                j += 1
        return result

    # The binary search pattern of find kth element
    while start < end:
        mid = start + (end - start) // 2
        index = getLessEqual(mid)
        if index < k:
            start = mid + 1
        else:
            end = mid
    return start

if __name__=="__main__":
    matrix = [[1,  5,  9],[10, 11, 13],[12, 13, 15]]
    k = 8
    print(kthSmallest2(matrix, k))
