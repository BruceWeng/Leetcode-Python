"""
Find the kth largest element in an unsorted array. Note that it is the kth largest
element in the sorted order, not the kth distinct element.
For example,
Given [3,2,1,5,6,4] and k = 2, return 5.

Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.
"""
"""
Algorithm:
Max-Heap:
1. Push each num in Max-Heap, T: O(n)
2. Pop k times to get kth largest element, each cost T: O(logn)
T: O(n + klogn), worst case, when k = n, O(nlogn)
S: O(n)

Min-Heap: (Save space)
1. Push first kth elements in Min-Heap, T: O(k)
2. Compare heap root and nums[i], i in range(k, len(nums) - 1), if nums[i] > root, heap.pop, heap.push(nums[i]) to leave kth largest element in Min-Heap, return heap.peek
T: O(k + (n - k)logk), worst case, when k = n, O(nlogn)
S: O(k)
"""
"""
Max-Heap Solution:
@param {int[]} nums
@param {int} k
@return {int}
"""
import heapq # Min-Heap
def findKthLargest(nums, k):
    # heapq.heapify(list)             # for a min heap
    # heapq._heapify_max(list)        # for a maxheap!!
    heap = []
    result = 0

    # Put negative num in heap
    for num in nums:
        heapq.heappush(heap, -num)

    for _ in range(k):
        result = -heapq.heappop(heap)

    return result

"""
Min-Heap Solution:
@param {int[]} nums
@param {int} k
@return {int}
"""
import heapq # Min-Heap
def findKthLargest2(nums, k):
    heap = []
    index = 0
    for i in range(k):
        heapq.heappush(heap, nums[i])
        index = i

    for j in range(index + 1, len(nums)):
        if nums[j] > heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, nums[j])

    return heap[0]

"""
Quick selection Solution:
@param {int[]} nums
@param {int} k
@return {int}
"""
def findKthLargest3(nums, k):
    pivot = nums[0]
    tail = 0

    for i in range(1, len(nums)):
        if nums[i] > pivot:
            tail += 1
            nums[tail], nums[i] = nums[i], nums[tail]

    nums[tail], nums[0] = nums[0], nums[tail]

    if tail + 1 == k:
        return pivot
    elif tail + 1 < k:
        return findKthLargest(nums[tail+1:], k - tail - 1)
    else:
        return findKthLargest(nums[:tail], k)  #excluding pivot

if __name__=="__main__":
    print(findKthLargest2([3,2,1,5,6,4], 2)) # 5
