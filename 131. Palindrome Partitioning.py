"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
"""
"""
Algorithm: DFS
0: Declare result[] to store validAns
1. Write a recursion helper function(subStr: str, validAns: []) to do DFS
(Free to pass subStr rather than index, since validAnswers has already use O(n) space)
2. helper(subStr, validAns):
    1. Termination condition: if len(subStr) == 0: copy validAns to new array and
    push the new array to result
    2. Recursive condition:
        for i in range(len(subStr)):
            prefix = subStr[:i+1]
            if prefix == prefix[::-1]:
                validAns.append(prefix)
                helper(subStr[i+1:], validAns)
                validAns.pop()
3. Call helper(s, [])
4. return result

Ex:"aab"
(A)
helper("aab", [])
subStr = "aab"
i = 0
prefix = "a"
Valid palindrome
validAns = ["a"]

(A.0)
helper("ab", ["a"])
subStr = "ab"
i = 0
prefix = "a"
Valid palindrome
validAns = ["a", "a"]

(A.0.0)
helper("b", ["a", "a"])
subStr = "b"
i = 0
prefix = "b"
Valid palindrome
validAns = ["a", "a", "b"]

(A.0.0.0)
helper("", ["a", "a", "b"])
subStr = ""
len(subStr) == 0
result = [
    ["a", "a", "b"]
]
return

(A.0.0)
subStr = "b"
Pop last element in validAns
validAns = ["a", "a"]
for loop end
return

(A.0)
subStr = "ab"
Pop last element in validAns
validAns = ["a"]
i = 1
prefix = "ab"
Not valid palindrome
continue
for loop end
return

(A)
subStr = "aab"
Pop last element in validAns
validAns = []
i = 1
prefix = "aa"
valid palindrome
validAns = ["aa"]

(A.1)
helper("b", ["aa"])
subStr = "b"
i = 0
prefix = "b"
Valid palindrome
validAns = ["aa", "b"]

(A.1.0)
helper("", ["aa", "b"])
subStr = ""
len(subStr) == 0
result = [
    ["a", "a", "b"],
    ["aa", "b"]
]
return

(A.1)
subStr = "b"
Pop last element in validAns
validAns = ["aa"]
for loop end
return

(A)
subStr = "aab"
Pop last element in validAns
validAns = []
i = 2
prefix = ""
Not valid palindrome
continue
for loop end
return

return result

T:
    helper: O(2^n),
    isPalindrome: O(n),
    total: O(n*2^n)
S:
    helper: O(2^n),
    isPalindrome: O(n),
    total: O(n*2^n)

Backtracking Summary:
1. Each node represent one helper call(subStr, validAns)
2. Use for loop in helper to generate child node
3. Use validAns.pop() after recursive call to cover validAns to parent condition
4. Use len(subStr) == 0 as termination condition to add validAns to result
"""
"""
@param {str} s
@return {[[str]]}
"""
def partition(s):
    if len(s) == 0:
        return []

    result = []

    def helper(subStr, validAns):
        if len(subStr) == 0:
            result.append(list(validAns))
            return

        for i in range(len(subStr)):
            prefix = subStr[:i+1]
            # isPalindrome T: O(n), S: O(n)
            if prefix == prefix[::-1]:
                validAns.append(prefix)
                helper(subStr[i+1:], validAns)
                validAns.pop()

    helper(s, [])
    return result
