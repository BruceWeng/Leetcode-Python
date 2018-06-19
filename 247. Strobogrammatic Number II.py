"""
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Find all strobogrammatic numbers that are of length = n.

Example:

Input:  n = 2
Output: ["11","69","88","96"]
"""
"""
Algorithm: Recursion
Base case:
if n == 1: return ["0", "1", "8"]
if n == 2: return ["11", "69", "88", "96", "00"]

Recursive case:
Odd: n % 2 == 1
Can be retrieved by inserting ["0", "1", "8"] to the middle of sol of n == 2
call func(n-1)
Even: n % 2 == 0
Can be retrieved by inserting ["11", "69", "88", "96", "00"] to the middle of sol of n == 2
call func(n-2)

ex: n = 5

previous = func(4), midCandidate = oddMidCandidate

n = 4

previous = func(2), mid Candidate = evenMidCandidate
preMid = (n-1) / 2
for char in midCandidate:
    for subChar in sub:
        result.appedn(sub[:preMid] + char + sub[preMide:])
return result
"""
"""
@param {int} n
@return {str[]}
"""
def findStrobogrammatic(n):
    evenMidCandidate = ["11", "69", "88", "96", "00"]
    oddMidCandidate = ["0", "1", "8"]
    if n == 1:
        return oddMidCandidate
    if n == 2:
        return evenMidCandidate[:-1]
    if n % 2 == 1:
        previous = self.findStrobogrammatic(n-1)
        midCandidate = oddMidCandidate
    else:
        previous = self.findStrobogrammatic(n-2)
        midCandidate = evenMidCandidate

    preMid = (n-1)/2
    result = []
    for char in midCandidate:
        for subChar in previous:
            result.append(subChar[:preMid] + char + subChar[preMid:])
    return result
