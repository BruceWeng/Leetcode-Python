"""
Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true

Note: It is intended for the problem statement to be ambiguous. You should gather
all requirements up front before implementing one.

Update (2015-02-10):
The signature of the C++ function had been updated. If you still see your function
signature accepts a const char * argument, please click the reload button to reset
your code definition.
"""
"""
Solution1: Exception
try:
    float(s)
    return true
except:
    return false

Solution2: Deterministic Finite Automaton (DFA)
Look up the DFA diagram @
https://leetcode.com/problems/valid-number/discuss/23728/A-simple-solution-in-Python-based-on-DFA

1. Dclare states in array of objects(key: category(digit, sign, e, ".", blank))
2. Construct states diagram
3. if char not in states[currState].keys(), return False
4. if currState(last state) not in [3, 5, 8, 9], return False
5. Return true

T: O(n)
S: O(1)
"""
def isNumber(s):
    states = [
        {},
        {"blank": 1, "sign": 2, "digit": 3, ".": 4}, # state 1 (q1)
        {"digit": 3, ".": 4},                        # state 2 (q2)
        {"digit": 3, ".": 5, "e": 6, "blank": 9},    # state 3 (q3)
        {"digit": 5},                                # state 4 (q4)
        {"digit": 5, "e": 6, "blank": 9},            # state 5 (q5)
        {"sign": 7, "digit": 8},                     # state 6 (q6)
        {"digit": 8},                                # state 7 (q7)
        {"digit": 8, "blank": 9},                    # state 8 (q8)
        {"blank": 9}                                 # state 9 (q9)
    ]

    currState = 1
    for c in s:
        if c >= "0" and c <= "9":
            c = "digit"
        if c == " ":
            c = "blank"
        if c in ["+", "-"]:
            c = "sign"
        if c not in states[currState].keys():
            return False
        currState = states[currState][c]

    if currState not in [3, 5, 8, 9]:
        return False

    return True
