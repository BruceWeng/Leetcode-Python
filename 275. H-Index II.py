"""
Given an array of citations in ascending order (each citation is a non-negative
integer) of a researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if
h of his/her N papers have at least h citations each, and the other N − h papers
have no more than hcitations each."

Example:

Input: citations = [0,1,3,5,6]
Output: 3
Explanation: [0,1,3,5,6] means the researcher has 5 papers in total and each of them had
             received 0, 1, 3, 5, 6 citations respectively.
             Since the researcher has 3 papers with at least 3 citations each and the remaining
             two with no more than 3 citations each, his h-index is 3.
Note: If there are several possible values for h, the maximum one is taken as the h-index.
"""
"""
Algorithm: Binary Search
1. Do binary search:
    if citation[mid] == len - mid, return len - mid (There is mid elements with citation >= mid)
    if citation[mid] < len - mid, target mid on the right hand side, start = mid
    else: end = mid
2. Final check for remaining two elements: (starting from start because choose maximum h-index)
    if citation[start] > len - start: return len - start
    if citation[end] > len - end: return len - end
    else: return len - end - 1

T: O(logn)
S: O(1)
"""
"""
@param {int[]} citations
@return {int}
"""
def hIndex(citations):
    if citations == None or len(citations) == 0:
        return 0

    n = len(citations)
    start = 0
    end = n - 1

    while start + 1 < end:
        mid = start + (end - start) // 2
        if citations[mid] == n - mid:
            return n - mid
        elif citations[mid] < n - mid:
            start = mid
        else:
            end = mid

    if citations[start] >= n - start:
        return n - start

    if citations[end] >= n - end:
        return n - end

    return n - end - 1
