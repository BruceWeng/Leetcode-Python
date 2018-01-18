"""
Given a string, find the first non-repeating character in it and return it's
index. If it doesn't exist, return -1.

Examples:
s = "leetcode"
return 0.

s = "loveleetcode",
return 2.

* Ternary: Use if...else instead of ?...:
"""
"""
@params {string} s
@return {int}
"""
class Character:
    def __init__(self, index):
        self.index = index
        self.times = 1
def firstUniqChar(s):
    if s == None or len(s) == 0:
        return -1

    table = {} # key: char, value: Character(index)
    for i, char in enumerate(s):
        if char not in table:
            table[char] = Character(i)
        else:
            table[char].times += 1

    index = len(s)
    for key in table:
        if table[key].times == 1:
            index = min(index, table[key].index)
    # Ternary: Use if...else instead of ?...:
    return -1 if index == len(s) else index
