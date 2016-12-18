class Solution(object):
    def intersect(self, nums1, nums2):
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
                cache[number] = 1
            else:
                cache[number] += 1

        for number2 in nums2:
            if number2 not in cache:
                continue
            if cache[number2] > 0:
                result.append(number2)
                cache[number2] -= 1

        return result
