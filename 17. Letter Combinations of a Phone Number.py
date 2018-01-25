"""
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

    1   2   3
       abc def
    4   5   6
   ghi jkl mno
    7   8   9
  pqrs tuv wxyz
        0
"""
"""
Algorithm:
                     ""
          /          |          \
        "a"         "b"         "c"
      /  |  \     /  |  \     /  |  \
    "d" "e" "f" "d" "e" "f" "d" "e" "f"

1. define dfs function accept sliced digits and current letter combinations
2. dfs:
    a. base case:
        if digits is empty, result.append(current), return
    b. recursive case:
        for c in table(digits[0]):
            dfs(digits[1:], current + c)
"""
"""
@param {string} digits
@return {string[]}
"""
def letterCombinations(digits):
    if len(digits) == 0:
        return []

    table = {
    "1": "",
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
    "0": ""
    }

    result = []

    def dfs(digits, current):
        if not digits:
            result.append(current)
            return
        for c in table[digits[0]]:
            dfs(digits[1:], current + c)

    dfs(digits, "")
    return result



if __name__=="__main__":
    print(letterCombinations("23")) # ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
