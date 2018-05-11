"""
Given an arbitrary ransom note string and another string containing letters from
all the magazines, write a function that will return true if the ransom note can
be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
"""
"""
Algorithm:
1. Declare a int array for 26 chars, to represent the how many times the char used
in magazine
2. Iterate magazine and increase arr[ord(i) - ord("a")]
3. Iterate ransomNote and return false if arr[ord(j) - ord("a")] < 0
4. else return true
"""
"""
@param {string} ransomNote （勒索信）
@param {string} magazine
@return {bool}
"""
def canConstruct(ransomNote, magazine):
    charCount = [0 for i in range(26)]
    for i in magazine:
        charCount[ord(i) - ord("a")] += 1

    for j in ransomNote:
        charCount[ord(j) - ord("a")] -= 1
        if charCount[ord(j) - ord("a")] < 0:
            return False

    return True
