"""
You are a product manager and currently leading a team to develop a new product.
Unfortunately, the latest version of your product fails the quality check.
Since each version is developed based on the previous version, all the versions
after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first
bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version
is bad. Implement a function to find the first bad version. You should minimize
the number of calls to the API.
"""
"""
Algorithm: Binary Search
1. end = mid condition: isBadVersion(n) == True, first badVersion is in RHS
2. start = mid condition: isBadVersion(n) == False, fist badVersion is in LHS
3. if isBadVersion(start): return start, otherwise return end
"""

"""
@param {int} n
@return {int}
"""
# def isBadVersion(version):

def firstBadVersion(n):
    if n <= 0: return -1

    start = 1
    end = n

    while start + 1 < end:
        mid = start + (end - start) // 2
        # Need to evaluate bad condition first
        if isBadVersion(mid):
            end = mid
        else:
            start = mid

    return start if isBadVersion(start) else end
