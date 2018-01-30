"""
Objection: find all combination from the letters on the phone
"""
"""
Ex:
Input: "23",
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
"""
"""
Corner cases:
1. "", None -> []
"""
"""
Algorithm:
1.
                ""
      /          |          \
    "a"         "b"        "c"
  /  |  \       /|\       / | \

"d" "e" "f" "d" "e" "f" "d" "e" "f"
2. traverse(current, s)
  a. base case:
    when not s: result.append(current)
  b. recursion:
    iterate char in the hass table: traverse(current + char, s[1:])
3. return result
"""
"""
@param {stirng} s: string of integer
@return {string[]}
"""
def phone_letter_combination(s):
  if len(s) == 0 or s == None:
    return []

  result = []

  hash_table = {
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

  def traverse(current, s):
    if not s:
      result.append(current)
      return

    for char in hash_table[s[0]]:
      traverse(current + char, s[1:])

  traverse("", s)
  return result

if __name__=="__main__":
  test1 = "23"
#   print(phone_letter_combination(test1))


"""
The gray code is a binary numeral system where two successive values differ in only one bit.
Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.
For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:
00 - 0 01 - 1 11 - 3 10 - 2
"""
"""
Corner case:
1. 0 < n < 1000
"""
"""
Algorithm:
n = 1: [0, 1]
n = 2: [00, 01, 11, 10], mask = 10
n = 3: [000, 001, 011, 010, 110, 111, 101, 100], mask = 100

1. result = [0]
2. Iterate all elements in result in reverse order, result.append(element | 1 << i)
3. return result
"""
"""
@param {int} n
@return {int[]}
"""

def gray_code(n):
  result = [0]


  for i in range(n):
    size = len(result)
    for j in range(size - 1, -1, -1):
      result.append(result[j] | 1 << i)

  return result

if __name__=="__main__":
  print(gray_code(2))
  print(gray_code(3))
