#Solution 1: brute force
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return n
        i = 1
        while n - i >= 0:
            n -= i
            i += 1

        return i - 1


#Solution 2: binary search
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return n

        start = 1
        end = n
        while start + 1 < end:
            mid = start + (end - start) / 2
            if (mid * (mid + 1))/2 == n:
                return mid
            elif (mid * ( mid + 1))/2 < n:
                start = mid
            else:
                end = mid

        return start


#Solution 3: math
# x(x+1) = 2n
# x = int((-1 + sqrt(1 + 8*n))/2)
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int((-1 + math.sqrt(1 + 8 * n)) / 2)
