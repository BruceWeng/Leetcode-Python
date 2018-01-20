"""

All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

For example,
Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",

Return:
["AAAAACCCCC", "CCCCCAAAAA"].
"""
"""
@params {string} s
@return {string[]}
T: O(n), S: O(n)
"""
def findRepeatedDnaSequences(s):
    if s == None or len(s) == 0:
        return []
    result = []
    # Look for all substring with length 10, if table[substring] == 1,
    # table[substring] += 1, else table[substring] = 1
    table = {}
    for i in range(0, len(s) - 9):
        substring = s[i:i + 10]
        if substring in table:
            if table[substring] == 1:
                table[substring] += 1
                result.append(substring)
        else:
            table[substring] = 1
    return result
