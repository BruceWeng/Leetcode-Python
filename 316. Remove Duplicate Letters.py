"""
Given a string which contains only lowercase letters, remove duplicate letters
so that every letter appear once and only once. You must make sure your result
is the smallest in lexicographical order among all possible results.

Note: smallest in lexicographical order
input: [a, b, c]
output: {a, ab, abc, b, bc, c}

Example 1:

Input: "bcabc"
Output: "abc"

Example 2:

Input: "cbacdcbc"
Output: "acdb"
"""
"""
Algorithm:
1. Declare int[26] count to store counts of character frequency
2. Declare a bool[26] visited store is the char is visited
3. Declare a stack to maintain the result is the smallest lexicographical order
4. Maintain stack:
    0. count[ord(char) - ord("a")] -= 1
    a. stack.push(char), visited[ord(char) - ord("a")] = true
    b. if visited[ord(char) = ord("a")]: continue
    c. if last element in stack is larger than current char and there is still
       element in the input (count[ord(stack[-1]) - ord("a")]) == true):
         visited[stack[-1]] = false
         stack.pop()
5.convert stack to string and return result

T: O(n)
S: O(1)
"""
"""
@param {str} s
@return {str}
"""
def removeDuplicateLetters(s):
    if s == None or len(s) == 0:
        return ""

    count = [ 0 for _ in range(26)]
    for char in s:
        count[ord(char) - ord("a")] += 1

    visited = [False for _ in range(26)]
    stack = []

    # Maintain stack
    for char in s:
        # Remember to decrement count[ord(char) - ord("a")] first, so that we
        # can correctly count following counts for the char
        count[ord(char) - ord("a")] -= 1
        if visited[ord(char) - ord("a")]:
            continue

        while len(stack) and ord(stack[-1]) > ord(char) and count[ord(stack[-1]) - ord("a")] > 0:
            visited[ord(stack[-1]) - ord("a")] = False
            stack.pop()

        stack.append(char)
        visited[ord(char) - ord("a")] = True

    return "".join(stack)
