"""
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".

Note:
The vowels does not include the letter "y".
"""
"""
Algorithm:
1. Declare vowels in upper and lower cases
2. Convert string to char array
3. Use two pointers start and end in while to reverse the vowels
4. Convert char array to string and return
T: O(n)
S: O(n)
"""
"""
@param {string} s
@return {string}
"""
def reverseVowels(s):
    if s == None or len(s) == 0:
        return ""

    vowels = "aeiouAEIOU"
    charArray = list(s)
    start = 0
    end = len(s) - 1

    while start < end:
        while start < end and charArray[start] not in vowels:
            start += 1

        while start < end and charArray[end] not in vowels:
            end -= 1

        temp = charArray[start]
        charArray[start] = charArray[end]
        charArray[end] = temp
        start += 1
        end -= 1

    return "".join(charArray)
