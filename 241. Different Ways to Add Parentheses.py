"""
Given a string of numbers and operators, return all possible results from computing
all the different possible ways to group numbers and operators.
The valid operators are +, - and *.

Example 1:

Input: "2-1-1"
Output: [0, 2]
Explanation:
((2-1)-1) = 0
(2-(1-1)) = 2
Example 2:

Input: "2*3-4*5"
Output: [-34, -14, -10, -10, 10]
Explanation:
(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10
"""
"""
Algorithm: Recursion + memorization
0. Use hashMap(subStr:str, computedResult:int) to memorize computed results
1. Iterate input:
    if input[i] in '+-*':
        iterate part1 from helper(s[:i])
            iterate part2 from helper(s[:i+1])
            # Exclude operator at i
            Do the operation
2. Handle the case that only number exists in input
3. Update hashMap[input] = result
4. return result

T: Two recursion call: O(3^n)
S: O(3^n)
"""
"""
@param {str} input
@return {int[]}
"""
def diffWaysToCompute(input):
    # step 0
    hashMap = {}
    def helper(input):
        if input in hashMap:
            return hashMap[input]

        result = []
        # step 1
        for i in range(len(input)):
            if input[i] in '+-*':
                left = input[:i]
                right = input[i+1:]
                leftList = helper(left)
                rightList = helper(right)
                for a in leftList:
                    for b in rightList:
                        if input[i] == '+':
                            result.append(a + b)
                        elif input[i] == '-':
                            result.append(a - b)
                        elif input[i] == '*':
                            result.append(a * b)
        # step 2
        if len(result) == 0:
            result.append(int(input))

        # step 3
        hashMap[input] = result

        #step 4
        return result

    return helper(input)
