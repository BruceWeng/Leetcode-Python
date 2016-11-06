class Solution:
    """
    @param nums: A list of Integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        # write your code here
        if nums == None:
            return []

        if nums == []:
            return [[]]

        array = []
        result = []

        def helper(result, array, nums):
            if nums == []:
                result += [array]
            else:
                for i in range(len(nums)):
                    newArray = array + [nums[i]]
                    newNums = nums[:i] + nums[i+1:]
                    helper(result, newArray, newNums)

        helper(result, array, nums)
        return result

    # Subset pattern
    def permute2(self, nums):
        array = []
        result = []
        if nums == None:
            return result

        def helper(result, array, nums):
            if len(array) == len(nums):
                result.append(list(array))
                return

            for i in range(len(nums)):
                if nums[i] not in array:
                    array.append(nums[i])
                    helper(result, array, nums)
                    array.pop()

        helper(result, array, nums)
        return result

solution = Solution()
test1 = [1, 2, 3]
print(solution.permute2(test1))
