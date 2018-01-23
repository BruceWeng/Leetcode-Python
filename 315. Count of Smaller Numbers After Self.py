"""
You are given an integer array nums and you have to return a new counts array.
The counts array has the property where counts[i] is the number of smaller elements
to the right of nums[i].

Example:
Given nums = [5, 2, 6, 1]

To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.

Return the array [2, 1, 1, 0].
"""
"""
Algorithm:
interval_index:         [0, 1, 2, 3, 4, 5, 6]
initial interval_value: [0, 0, 0, 0, 0, 0, 0]
traverse starting from last element:
1:  result[i] = [0:0].count = 0
    interval_value[1] += 1: [0 ,1, 0, 0, 0, 0, 0]
6:  result[i] = [0:5].count = 1
    interval_value[6] += 1: [0, 1, 0, 0, 0, 0, 1]
2:  result[i] = [0:2].count = 1
    interval_value[2] += 1: [0, 1, 1, 0, 0, 0, 1]
5:  result[i] = [0:4].count = 2
    interval_value[5] += 1: [0, 1, 1, 0, 0, 1, 1]
result = [2, 1, 1, 0]
"""
"""
Complexity: T: O(nlogn), S: O(n)
"""
"""
@param {int[]} nums
@return {int[]}
"""
class SegmentTreeNode:
    def __init__(self, start, end, count):
        self.start = start
        self.end = end
        self.count = count
        self.left = None
        self.right = None

class SegmentTree:
    def __init__(self):
        pass

    """
    @param {int} start
    @param {int} end
    @return {SegmentTreeNode}
    """
    def build(self, start, end):
        # check corner case
        if start > end: return

        root = SegmentTreeNode(start, end, 0)
        if start != end:
            mid = (start + end) // 2
            root.left = self.build(start, mid)
            root.right = self.build(mid + 1, end)
        else:
            root.count = 0

        return root

    """
    @param {SegmentTreeNode} root
    @param {int} start
    @param {int} end
    @return {int} count
    """
    def query(self, root, start, end):
        # find the interval
        if root.start == start and root.end == end:
            return root.count

        mid = (root.start + root.end) // 2
        left_count = 0
        right_count = 0

        # left subtree
        if root.left and start <= mid:
            if mid < end: # split
                left_count = self.query(root.left, start, mid)
            else:
                left_count = self.query(root.left, start, end)

        # right subtree
        if root.right and mid < end:
            if start <= mid:
                right_count = self.query(root.right, mid + 1, end)
            else:
                right_count = self.query(root.right, start, end)

        return left_count + right_count

    """
    @param {SegmentTreeNode} root
    @param {int} index
    @param {int} value
    @return {void}
    """
    def modify(self, root, index, value):
        if root.start == index and root.end == index:
            root.count += value
            return
        # search index
        mid = (root.start + root.end) // 2
        if root.start <= index and index <= mid:
            self.modify(root.left, index, value)

        if index <= root.end and mid < index:
            self.modify(root.right, index, value)

        # update parant value
        root.count = root.left.count + root.right.count

def countSmaller(nums):
    if nums == None or len(nums) == 0:
        return []
    min_value = min(nums)
    max_value = max(nums)
    segment_tree = SegmentTree()
    root = segment_tree.build(min_value, max_value)
    result = [0] * len(nums)
    for i in range(len(nums) - 1, -1, -1):
        count = segment_tree.query(root, min_value, nums[i] - 1)
        segment_tree.modify(root, nums[i], 1)
        result[i] = count
    return result

if __name__=="__main__":
    test = [5, 2, 6, 1]
    print(countSmaller(test)) # [2, 1, 1, 0]
