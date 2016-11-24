# Solution: every number x bitwise shift one left from x / 2
# ex: 10: 1010, 5: 101, therefore the even number have same 1's, odd number have 1's + 1
# result[i] = result[i >> 1] + (i & 1)
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        result = [0] * (num + 1)
        for i in range(1, num + 1):
            result[i] = result[i >> 1] + (i & 1)

        return result
