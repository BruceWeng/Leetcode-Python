"""
You are playing the following Flip Game with your friend: Given a string that
contains only these two characters: + and -, you and your friend take turns to
flip two consecutive "++" into "--". The game ends when a person can no longer
make a move and therefore the other person will be the winner.

Write a function to determine if the starting player can guarantee a win.

For example, given s = "++++", return true. The starting player can guarantee a
win by flipping the middle "++" to become "+--+".

Follow up:
Derive your algorithm's runtime complexity.
"""
"""
Algorithm:
Solution 1: Backtracking
1. Replace "++" in the s to "--" and pass the result string to canWin recursively,
if !canWin(s) (for 2P): return true (for 1P)
2. Return false (for 1P)

Time complexity: length of n will contains n - 1 ways to replace "++" to "--",
T: (n-1)(n-3)(n-5)... = n!! double factorial
ex: 9!! = 9*7*5*3*1
S: n!!

Solution 2: Memorization
1. Declare a hashmap with index of string, value of boolean
2. Create a inner function bool canWin(newString, hashmap)
3. a. Replace "++" in the s to "--" and pass the result string to canWin recursively,
    if !canWin(s) (for 2P): return true (for 1P)
   b. Return false (for 1P)

T: 2^n ???
S: 2^n
"""
"""
@param {string} s
@return {bool}
"""
def canWin(s):
    if s == None or len(s) == 0:
        return False

    hashmap = {} # index: string, value: bool

    def canWin(s, hashmap):
        value = hashmap.get(s)
        if value:
            return value

        for i in range(1, len(s)):
            if s[i] == "+" and s[i-1] == "+":
                new_s = s[:i-1] + "--" + s[i+1:]
                if not canWin(new_s, hashmap):
                    hashmap[s] = True
                    return True

        hashmap[s] = False
        return False

    return canWin(s, hashmap)
