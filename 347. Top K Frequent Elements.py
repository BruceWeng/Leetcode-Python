class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        # 1.Init dict of [number: count]
        # 2.Init an array with objects sorted by count
        # 3.Append top k count nums into result array
        # T: O(nlogn) S: O(n)
        if not nums or len(nums) == 0 or k == 0:
            return []

        cache = {}
        for num in nums:
            if num not in cache:
                cache[num] = 1
            else:
                cache[num] += 1
        sortByFreq = sorted(cache.items(), key=lambda x:x[1], reverse=True)
        result = [ sortByFreq[i][0] for i in range(k) ]
        return result

test1 = [1,1,1,2,2,3,4,4,4,4]
sol = Solution()
print sol.topKFrequent(test1, 3)
