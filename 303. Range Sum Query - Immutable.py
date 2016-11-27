class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        if len(nums) == 0:
            self.preSum = []
        else:
            self.preSum = [0 for i in range(len(nums))]
            self.preSum[0] = nums[0]
            for i in range(1, len(nums)):
                self.preSum[i] = nums[i] + self.preSum[i - 1]

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            return self.preSum[j]
        else:
            return self.preSum[j] - self.preSum[i - 1]


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)

num = NumArray([1, 2, 3])
print num.preSum
