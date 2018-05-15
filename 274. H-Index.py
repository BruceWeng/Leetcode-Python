"""
Given an array of citations (each citation is a non-negative integer) of a
researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if
h of his/her N papers have at least h citations each, and the other N − h papers
have no more than h citations each."

Example:

Input: citations = [3,0,6,1,5]
Output: 3
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had
             received 3, 0, 6, 1, 5 citations respectively.
             Since the researcher has 3 papers with at least 3 citations each and the remaining
             two with no more than 3 citations each, his h-index is 3.
Note: If there are several possible values for h, the maximum one is taken as the h-index.
"""
"""
Algorithm:
Solution 1: Brute Force
1. Iterate array with i from 1 to len(array), to check there are i elements greater and equals to i
2. Overwrite h if there is greater h-index i
3. return h

T: O(n^2)
S: O(1)

Solution 2: Counting Sort
1. Declare a counts array with length n + 1 used to store counts of elements
    index: element, value: counts
2. Iterate array, if element is greater than array length, increment at array index n
3. Iterate counts array from end to front, h += counts[i], if h >= i, return i

T: O(n)
S: O(n)
"""
"""
@param {int[]} citations
@return {int}
"""
def hIndex(citations):
    if citations == None or len(citations) == 0:
        return 0

    n = len(citations)
    counts = [0] * (n + 1)
    for c in citations:
        if c >= n:
            counts[n] += 1
        else:
            counts[c] += 1

    h = 0
    for i in range(n, -1, -1):
        h += counts[i]
        if h >= i:
            return i

    return 0
