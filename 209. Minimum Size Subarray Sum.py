class Solution:
    if nums == None or len(nums) == 0:
            return 0

        n = len(nums)
        left = 0
        right = 0
        total = 0
        result = n + 1
        while right < n:
            while right < n and total < s:
                total += nums[right]
                right += 1

            while left < right and total >= s:
                result = min(result, right - left)
                total -= nums[left]
                left += 1


        if result == n + 1:
            return 0
        else:
            return result
