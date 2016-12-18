class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1) == 0 or len(nums2) == 0:
            return []

        cache = {}
        result = []
        for number in nums1:
            if number not in cache:
                cache[number] = True

        for number2 in nums2:
            if number2 not in cache:
                continue
            if cache[number2] == True:
                result.append(number2)
                cache[number2] = False

        return result

test1 = [1]
test2 = [1, 1, 1]
sol = Solution()
print sol.intersection(test1, test2)
