"""
You are playing the following Flip Game with your friend: Given a string that
contains only these two characters: + and -, you and your friend take turns to
flip two consecutive "++" into "--". The game ends when a person can no longer
make a move and therefore the other person will be the winner.

Write a function to compute all possible states of the string after one valid move.

For example, given s = "++++", after one move, it may become one of the following states:

[
  "--++",
  "+--+",
  "++--"
]
If there is no valid move, return an empty list [].
"""
"""
Algorithm: Brute Force
1. Declare a result array stores possible states
2. Iterate input string starts from i = 0:
    if array[i] == "+" and array[i-1] == "+":
        concat array[:i-1] + "--" + array[i+1:]
        result.append(new state)
3. return result

T: O(n^2), slicing takes O(n)
S: O(n), result array
"""
"""
@param {string} s
@return {string[]}
"""
def generatePossibleNextMoves(s):
    if s == None or len(s) == 0:
        return []

    result = []
    for i in range(1, len(s)):
        if s[i] == "+" and s[i-1] == "+":
            result.append(s[:i-1] + "--" + s[i+1:])

    return result
